export type Node = 
  | AppDeclaration
  | ModelDeclaration 
  | DataDeclaration
  | ScreenDeclaration
  | ActionDeclaration;

export interface AppDeclaration {
  kind: 'AppDeclaration';
  name: string;
  title: string;
  declarations: Node[];
}

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
  defaultValue: Value | null;
  isOptional: boolean;
  enumValues?: string[]; // For 'in [...]' fields
}

export interface DataDeclaration {
  kind: 'DataDeclaration';
  datasets: DatasetDeclaration[];
}

export interface DatasetDeclaration {
  kind: 'DatasetDeclaration';
  name: string;
  type: string; // Model name
  instances: DataInstance[];
}

export interface DataInstance {
  kind: 'DataInstance';
  values: DataValue[];
}

export interface DataValue {
  kind: 'DataValue';
  name?: string; // Optional for positional values
  value: Value;
}

export interface ScreenDeclaration {
  kind: 'ScreenDeclaration';
  name: string;
}

export interface ActionDeclaration {
  kind: 'ActionDeclaration';
  name: string;
  parameters: Parameter[];
  statements: ActionStatement[];
}

export interface Parameter {
  kind: 'Parameter';
  name: string;
  type: TypeName;
  isOptional: boolean;
}

export interface ActionStatement {
  kind: 'CreateStatement';
  model: string;
  assignments: FieldAssignment[];
}

export interface FieldAssignment {
  kind: 'FieldAssignment';
  field: string;
  value: string;
}

export type TypeName = 'text' | 'num' | 'bool' | 'date' | string;

export type Value = string | number | boolean | Date | { kind: 'DatasetIndex', dataset: string, index: number };
