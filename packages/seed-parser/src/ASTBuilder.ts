import { SeedSpecVisitor } from './SeedSpecVisitor';
import { ModelDeclaration, FieldDeclaration, TypeName } from './ast';
import {
  ProgramContext,
  ModelDeclarationContext,
  FieldDeclarationContext,
} from './SeedSpecParser'; // Import from generated parser
import { AbstractParseTreeVisitor } from 'antlr4';

export class ASTBuilder
  extends AbstractParseTreeVisitor<any>
  implements SeedSpecVisitor<any>
{
  visitProgram(ctx: ProgramContext): ModelDeclaration[] {
    return ctx.modelDeclaration().map((modelCtx) => this.visit(modelCtx));
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
      defaultValue = this.visit(ctx.defaultValue()); // Simplified for now
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

  visitTypeName(ctx: any): TypeName {
    // Assuming basic types for now: text, num, bool
    return ctx.getText() as TypeName;
  }

  visitDefaultValue(ctx: any): any {
    // Simplified handling of default values for now
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
