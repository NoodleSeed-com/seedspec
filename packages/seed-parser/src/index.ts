import { CharStreams, CommonTokenStream } from 'antlr4';
import { SeedSpecLexer } from './SeedSpecLexer';
import { SeedSpecParser } from './SeedSpecParser';
import { ASTBuilder } from './ASTBuilder';

export function parseSeedSpec(input: string) {
  const chars = CharStreams.fromString(input);
  const lexer = new SeedSpecLexer(chars);
  const tokens = new CommonTokenStream(lexer);
  const parser = new SeedSpecParser(tokens);
  parser.buildParseTrees = true;
  const tree = parser.program();

  const builder = new ASTBuilder();
  const ast = builder.visit(tree);

  return ast;
}
