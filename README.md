# 🛡️ Sistema Biométrico de Detección de Fraude

Sistema de verificación de identidad mediante firma digital que detecta casos de fraude, suplantación y falsificación.

## 📋 Descripción

Proyecto desarrollado para **Code in Place 2024** que simula un sistema de ciberseguridad mediante biometría de firma digital.

## 🚀 Características

✅ Registro de usuarios con cédula y firma digital  
✅ Verificación de identidad con algoritmo de similitud  
✅ Detección de 3 tipos de fraude:
- Cédulas inválidas (formato incorrecto)
- Suplantación de identidad (cédula no coincide)
- Firma falsificada (similitud < 35%)

## 💻 Cómo usar

1. Ejecutar el programa:
```bash
python main.py
```

2. Menú principal:
   - **Opción 1**: Registrar identidad (nombre + cédula + firma)
   - **Opción 2**: Verificar identidad
   - **Opción 3**: Salir

3. Para registrar:
   - Ingresa nombre y cédula (10 dígitos)
   - Dibuja tu firma en el canvas
   - Presiona Enter

4. Para verificar:
   - Ingresa tu cédula
   - Dibuja tu firma nuevamente
   - El sistema detecta si es fraudulenta

## 🔒 Algoritmo de Detección

El sistema compara:
- Número de puntos de la firma
- Dimensiones (ancho y alto)
- Similitud mínima requerida: 35%

## 🛠️ Tecnologías

- Python 3.x
- Graphics Library (Code in Place)

## 👨‍💻 Autor

**Daniela Torres**  
Code in Place 2024 - Proyecto Final

## 📧 Contacto

GitHub: [@DanielaTorres1224](https://github.com/DanielaTorres1224)

---

⭐ Si te gustó este proyecto, dale una estrella!
```

---

## 📝 Pasos para subir:

1. **Copia el código de `main.py`** (todo lo de arriba)
2. En GitHub, click en **"Add file"** → **"Create new file"**
3. Nombre: `main.py`
4. Pega el código
5. Click en **"Commit new file"**

6. **Copia el código de `README.md`**
7. Click en **"Add file"** → **"Create new file"**
8. Nombre: `README.md`
9. Pega el contenido
10. Click en **"Commit new file"**

**¡Y listo!** Tu link es:
```
https://github.com/DanielaTorres1224/sistema-biometrico
