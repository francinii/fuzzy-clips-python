# FuzzyCLIPS Installation Guide

---

## Configuración del Entorno Virtual en Python

1. **Crear un entorno virtual**
   ```sh
   python -m venv .venv
   ```

2. **Activar el entorno virtual**
   - En Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

3. **Instalar dependencias**
   ```sh
   pip install -r requirements.txt
   ```


## Installation FuzzyCLIPS

### Requisitos
- [MinGW](https://sourceforge.net/projects/mingw/)
- [Guía de instalación](https://emasuriano.com/blog/2024-07-31-install-fuzzy-clips/)
- [Repositorio de FuzzyCLIPS](https://github.com/rorchard/FuzzyCLIPS)
- [Video tutorial](https://www.youtube.com/watch?v=GEZLjRSY_m8&t=50s&ab_channel=CharlyCimino)

### Instalación paso a paso

1. **Clonar el repositorio de FuzzyCLIPS**
   ```sh
   git clone https://github.com/rorchard/FuzzyCLIPS.git
   ```

2. **Instalar MinGW**
   - Seguir los primeros minutos del [video tutorial](https://www.youtube.com/watch?v=GEZLjRSY_m8&t=50s) para la instalación y configuración de la variable de entorno en Windows.
   - Descargar MinGW desde [este enlace](https://sourceforge.net/projects/mingw/).
   - Importante: Para evitar problemas, ejecutar desde `cmd`, no desde `PowerShell`.

3. **Modificar el archivo `Makefile.cl`**
   - Abrir `Makefile.cl` y cambiar la siguiente línea:
     ```sh
     CC = cc
     ```
     por:
     ```sh
     CC = gcc
     ```
   - También cambiar la línea:
     ```sh
     LIBS = -lm -ltermcap
     ```
     por:
     ```sh
     LIBS = -lm
     ```

4. **Compilar y ejecutar FuzzyCLIPS**
   - Seguir la guía detallada en [este enlace](https://emasuriano.com/blog/2024-07-31-install-fuzzy-clips/).
   - Para verificar la instalación, ejecutar en la terminal:
     ```sh
     fz_clips
     ```

### Uso de FuzzyCLIPS

Para cargar y ejecutar un archivo en FuzzyCLIPS, usar los siguientes comandos:
```sh
(load ./EJEMPLO_01.clp)
(reset)
(facts)
(rules)
(run)
(plot-fuzzy-value t + 0 100 3)
```

Si `fz_clips` se ejecuta correctamente, la instalación ha sido exitosa.


