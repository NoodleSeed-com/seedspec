import antlr4 from 'antlr4';
import { SeedSpecLexer } from './SeedSpecLexer';
import { SeedSpecParser } from './SeedSpecParser';
import { ASTBuilder } from './ASTBuilder';

const { CommonTokenStream, InputStream } = antlr4;

export function parseSeedSpec(input: string) {
  const chars = new InputStream(input);
  const lexer = new SeedSpecLexer(chars);
  const tokens = new CommonTokenStream(lexer);
  const parser = new SeedSpecParser(tokens);
  parser.buildParseTrees = true;
  const tree = parser.program();

  const builder = new ASTBuilder();
  const ast = builder.visit(tree);

  return ast;
}
