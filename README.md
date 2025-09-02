📐 Calculadora de Expresiones
📖 Historia de Usuario

Como usuario quiero ingresar una operación matemática simple como 2 + 3 * 4 para obtener el resultado correcto, respetando el orden de operaciones.

✅ Criterios de Aceptación

2 + 3 * 4 → 14

(2 + 3) * 4 → 20

Si la expresión es inválida, debe devolver un error controlado.

🎯 Objetivo del Proyecto

Implementar una calculadora de expresiones que procese operaciones matemáticas, aplicando prácticas de Scrum + XP:

Scrum → Organización del equipo con roles (PO, Scrum Master, Developers).

XP → TDD, Pair Programming, Refactorización.

🛠 Tecnologías utilizadas

Lenguaje: Java (o el lenguaje que usen).

Pruebas: JUnit (para TDD).

Control de versiones: GitHub.

🚀 Funcionalidades

Evaluación de expresiones matemáticas.

Manejo de prioridad de operaciones (paréntesis, multiplicación, división, suma y resta).

Validación y manejo de errores en expresiones inválidas.

👥 Roles Scrum

Product Owner (PO): Define la historia de usuario y criterios de aceptación.

Scrum Master: Facilita el proceso Scrum, organiza dailys y retrospectivas.

Developers: Implementan la lógica, pruebas unitarias y refactorización.

🔬 Enfoque XP aplicado

TDD → primero se escriben las pruebas, luego el código.

Pair Programming → dos miembros trabajando en conjunto (driver y navigator).

Refactorización → limpieza de código y eliminación de duplicaciones en el parser.

📂 Estructura del repositorio
📦 calculadora-expresiones
 ┣ 📂 src/       # Código fuente
 ┣ 📂 test/      # Pruebas unitarias
 ┣ 📜 README.md  # Documentación del proyecto
 ┣ 📜 .gitignore
 ┗ 📜 LICENSE (opcional)

🧪 Ejemplo de ejecución

Entrada:

(2 + 3) * 4


Salida:

20
