export interface ModelDeclaration {
  kind: 'ModelDeclaration';
  name: string;
  fields: FieldDeclaration[];
}

export interface FieldDeclaration {
  kind: 'FieldDeclaration';
  name: string;
  type: TypeName;
  isTitle: boolean;
  defaultValue: any; // Simplified for now
  isOptional: boolean;
}

export type TypeName = 'text' | 'num' | 'bool';
