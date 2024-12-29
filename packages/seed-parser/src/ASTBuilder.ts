import { SeedSpecVisitor } from './SeedSpecVisitor';
import { ModelDeclaration, FieldDeclaration, TypeName } from './ast';
import {
  ProgramContext,
  ModelDeclarationContext,
  FieldDeclarationContext,
  TypeNameContext,
  DefaultValueContext,
} from './SeedSpecParser'; // Import from generated parser
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

  visitProgram(ctx: ProgramContext): ModelDeclaration[] {
    this.errors = []; // Reset errors
    const models = ctx
      .modelDeclaration()
      .map((modelCtx) => this.visit(modelCtx));

    if (this.errors.length > 0) {
      throw this.errors; // Throw collected errors
    }

    return models;
  }

  visitModelDeclaration(ctx: ModelDeclarationContext): ModelDeclaration {
    const name = ctx.IDENTIFIER().text;
    const fields = ctx
      .fieldDeclaration()
      .map((fieldCtx) => this.visit(fieldCtx));

    return {
      kind: 'ModelDeclaration',
      name,
      fields,
    };
  }

  visitFieldDeclaration(ctx: FieldDeclarationContext): FieldDeclaration {
    const name = ctx.IDENTIFIER().text;
    const type = this.visit(ctx.typeName()) as TypeName;
    const isTitle = !!ctx.KW_AS(); // Check if 'as title' is present
    const isOptional = !!ctx.QUESTION(); // Check if '?' is present

    let defaultValue = null;
    if (ctx.defaultValue()) {
      defaultValue = this.visit(ctx.defaultValue());
    }

    return {
      kind: 'FieldDeclaration',
      name,
      type,
      isTitle,
      defaultValue,
      isOptional,
    };
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
