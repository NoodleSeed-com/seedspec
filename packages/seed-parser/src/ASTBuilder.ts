import { SeedSpecVisitor } from './SeedSpecVisitor';
import { 
  Node, AppDeclaration, ModelDeclaration, FieldDeclaration, 
  DataDeclaration, ScreenDeclaration, ActionDeclaration,
  Parameter, ActionStatement, FieldAssignment, TypeName,
  Value, DatasetDeclaration, DataInstance, DataValue
} from './ast';
import {
  ProgramContext,
  AppDeclarationContext,
  ModelDeclarationContext,
  FieldDeclarationContext,
  DataDeclarationContext,
  ScreenDeclarationContext,
  ActionDeclarationContext,
  ParameterListContext,
  ActionStatementContext,
  TypeNameContext,
  DefaultValueContext,
  DatasetDeclarationContext,
  DataInstanceContext,
  DataValueContext
} from './SeedSpecParser';
import { AbstractParseTreeVisitor } from 'antlr4';
import { ErrorNode } from 'antlr4/tree/Tree';

class SyntaxError extends Error {
  line: number;
  column: number;

  constructor(line: number, column: number, message: string) {
    super(message);
    this.name = 'SyntaxError';
    this.line = line;
    this.column = column;
  }
}

export class ASTBuilder
  extends AbstractParseTreeVisitor<any>
  implements SeedSpecVisitor<any>
{
  errors: SyntaxError[] = [];

  visitErrorNode(node: ErrorNode) {
    const token = node.symbol;
    this.errors.push(
      new SyntaxError(
        token.line,
        token.column,
        `Syntax error: Unexpected token ${token.text}`,
      ),
    );
    return null;
  }

  visitProgram(ctx: ProgramContext): Node[] {
    this.errors = []; // Reset errors
    const declarations = ctx.declaration().map(decl => this.visit(decl));

    if (this.errors.length > 0) {
      throw this.errors;
    }

    return declarations;
  }

  visitAppDeclaration(ctx: AppDeclarationContext): AppDeclaration {
    const name = ctx.IDENTIFIER().text;
    const title = this.stripQuotes(ctx.STRING_LITERAL().text);
    const declarations = ctx.declaration().map(decl => this.visit(decl));

    return {
      kind: 'AppDeclaration',
      name,
      title,
      declarations
    };
  }

  visitModelDeclaration(ctx: ModelDeclarationContext): ModelDeclaration {
    const name = ctx.IDENTIFIER().text;
    const fields = ctx.fieldDeclaration().map(field => this.visit(field));

    return {
      kind: 'ModelDeclaration',
      name,
      fields,
    };
  }

  visitDataDeclaration(ctx: DataDeclarationContext): DataDeclaration {
    const datasets = ctx.datasetDeclaration().map(dataset => this.visit(dataset));
    
    return {
      kind: 'DataDeclaration',
      datasets
    };
  }

  visitDatasetDeclaration(ctx: DatasetDeclarationContext): DatasetDeclaration {
    const name = ctx.IDENTIFIER()[0].text;
    const type = ctx.IDENTIFIER()[1].text;
    const instances = ctx.dataInstance().map(instance => this.visit(instance));

    return {
      kind: 'DatasetDeclaration',
      name,
      type,
      instances
    };
  }

  visitDataInstance(ctx: DataInstanceContext): DataInstance {
    const values = ctx.dataValue().map(value => this.visit(value));

    return {
      kind: 'DataInstance',
      values
    };
  }

  visitDataValue(ctx: DataValueContext): DataValue {
    const value = this.visit(ctx.value());
    
    if (ctx.IDENTIFIER()) {
      return {
        kind: 'DataValue',
        name: ctx.IDENTIFIER().text,
        value
      };
    }

    return {
      kind: 'DataValue',
      value
    };
  }

  visitFieldDeclaration(ctx: FieldDeclarationContext): FieldDeclaration {
    const name = ctx.IDENTIFIER()[0].text;
    let type: TypeName;
    let enumValues: string[] | undefined;
    
    if (ctx.typeName()) {
      type = this.visit(ctx.typeName());
    } else if (ctx.IDENTIFIER().length > 1) {
      type = 'enum';
      enumValues = ctx.IDENTIFIER().slice(1).map(id => id.text);
    } else {
      throw new Error('Invalid field declaration');
    }

    const isTitle = ctx.KW_AS && ctx.KW_TITLE;
    const isOptional = !!ctx.QUESTION();
    const defaultValue = ctx.defaultValue() ? this.visit(ctx.defaultValue()) : null;

    return {
      kind: 'FieldDeclaration',
      name,
      type,
      isTitle,
      defaultValue,
      isOptional,
      enumValues
    };
  }

  visitScreenDeclaration(ctx: ScreenDeclarationContext): ScreenDeclaration {
    return {
      kind: 'ScreenDeclaration',
      name: ctx.IDENTIFIER().text
    };
  }

  visitActionDeclaration(ctx: ActionDeclarationContext): ActionDeclaration {
    const name = ctx.IDENTIFIER().text;
    const parameters = ctx.parameterList() ? 
      ctx.parameterList().parameter().map(param => this.visit(param)) :
      [];
    const statements = ctx.actionStatement().map(stmt => this.visit(stmt));

    return {
      kind: 'ActionDeclaration',
      name,
      parameters,
      statements
    };
  }

  private stripQuotes(str: string): string {
    return str.slice(1, -1);
  }

  visitTypeName(ctx: TypeNameContext): TypeName {
    return ctx.getText() as TypeName;
  }

  visitDefaultValue(ctx: DefaultValueContext): any {
    const text = ctx.getText();
    if (text.startsWith('"')) {
      return text.substring(1, text.length - 1); // Remove quotes
    } else if (text === 'true' || text === 'false') {
      return text === 'true';
    } else {
      return parseFloat(text); // Parse as number
    }
  }

  protected defaultResult(): any {
    return null;
  }
}
