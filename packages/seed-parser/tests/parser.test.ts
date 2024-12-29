import { parseSeedSpec } from '../src/index'; // Update with correct path
import { ModelDeclaration } from '../src/ast';

describe('SeedSpec Parser', () => {
  it('should parse a complete app declaration', () => {
    const input = `
      app TaskManager "Task Management App" {
        model Task {
          title text as title
          completed bool = false
        }

        data {
          Tasks: Task[] [
            { "First task", false },
            { "Second task", true }
          ]
        }

        screen Tasks
      }
    `;

    const ast = parseSeedSpec(input);
    expect(ast[0]).toEqual({
      kind: 'AppDeclaration',
      name: 'TaskManager',
      title: 'Task Management App',
      declarations: [
        {
          kind: 'ModelDeclaration',
          name: 'Task',
          fields: [
            {
              kind: 'FieldDeclaration',
              name: 'title',
              type: 'text',
              isTitle: true,
              defaultValue: null,
              isOptional: false
            },
            {
              kind: 'FieldDeclaration',
              name: 'completed',
              type: 'bool',
              isTitle: false,
              defaultValue: false,
              isOptional: false
            }
          ]
        },
        {
          kind: 'DataDeclaration',
          datasets: [{
            kind: 'DatasetDeclaration',
            name: 'Tasks',
            type: 'Task',
            instances: [
              {
                kind: 'DataInstance',
                values: [
                  { kind: 'DataValue', value: 'First task' },
                  { kind: 'DataValue', value: false }
                ]
              },
              {
                kind: 'DataInstance',
                values: [
                  { kind: 'DataValue', value: 'Second task' },
                  { kind: 'DataValue', value: true }
                ]
              }
            ]
          }]
        },
        {
          kind: 'ScreenDeclaration',
          name: 'Tasks'
        }
      ]
    });
  });

  it('should parse a simple model', () => {
    const input = `
      model User {
        name text
        age num
      }
    `;
    const ast = parseSeedSpec(input);

    expect(ast).toEqual([
      {
        kind: 'ModelDeclaration',
        name: 'User',
        fields: [
          {
            kind: 'FieldDeclaration',
            name: 'name',
            type: 'text',
            isTitle: false,
            defaultValue: null,
            isOptional: false,
          },
          {
            kind: 'FieldDeclaration',
            name: 'age',
            type: 'num',
            isTitle: false,
            defaultValue: null,
            isOptional: false,
          },
        ],
      },
    ]);
  });

  it('should handle optional fields and title fields', () => {
    const input = `
      model Product {
        name text as title
        description text?
        price num = 0
      }
    `;
    const ast = parseSeedSpec(input);

    expect(ast).toEqual([
      {
        kind: 'ModelDeclaration',
        name: 'Product',
        fields: [
          {
            kind: 'FieldDeclaration',
            name: 'name',
            type: 'text',
            isTitle: true,
            defaultValue: null,
            isOptional: false,
          },
          {
            kind: 'FieldDeclaration',
            name: 'description',
            type: 'text',
            isTitle: false,
            defaultValue: null,
            isOptional: true,
          },
          {
            kind: 'FieldDeclaration',
            name: 'price',
            type: 'num',
            isTitle: false,
            defaultValue: 0,
            isOptional: false,
          },
        ],
      },
    ]);
  });

  it('should report syntax errors', () => {
    const input = `
      model User {
        name text = 
      }
    `;

    expect(() => parseSeedSpec(input)).toThrowError(
      expect.arrayContaining([
        expect.objectContaining({
          line: 3,
          column: 19,
          message: expect.stringContaining('Syntax error'),
        }),
      ]),
    );
  });
});
