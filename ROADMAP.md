# Ledger — Roadmap QA Full Stack

> Regla de oro: cada fase termina en un estado funcional y demostrable, aunque no esté "completa".

## Fase 0 — Verificar lo que ya existe

- [X] Abrir la URL de Render y comprobar que responde (no 500, no "service unavailable")
- [X] Hacer login con Bruno contra la URL de producción (no local)
- [X] Ejecutar 2-3 requests clave de tu colección Bruno contra producción (crear gasto, listar, IDOR check)
- [X] Anotar en un `.md` cualquier cosa rota que encuentres

## Fase 1 — Cerrar los tests de API que ya tenías empezados

*(no arranques el frontend hasta que esto esté verde)*

- [X] Escribir `conftest.py` con fixtures de usuario + token
- [X] Test: registro de usuario
- [X] Test: login devuelve token válido
- [X] Test: login con credenciales malas falla
- [ ] Test: crear gasto (happy path)
- [ ] Test: listar gastos del usuario
- [ ] Test: usuario A no puede ver/editar gasto de usuario B (IDOR)
- [ ] Test: crear gasto con categoría de otro usuario falla
- [ ] Ejecutar `pytest-cov` y ver qué % de cobertura tienes
- [ ] Commit + push

## Fase 2 — Frontend mínimo (esqueleto)

- [ ] `npm create vite@latest` con template React
- [ ] Configurar variable de entorno para la URL de la API
- [ ] Página de Login: formulario simple, sin estilos
- [ ] Login: guardar token en memoria (state), no en localStorage todavía
- [ ] Petición de prueba: al loguear, hacer un `fetch` a `/api/expenses/` y hacer `console.log` del resultado
- [ ] Confirmar en consola del navegador que llega el JSON correcto

## Fase 3 — Conectar de verdad backend + frontend

- [ ] Configurar CORS en Django (`django-cors-headers`) para permitir el origen del frontend
- [ ] Crear un pequeño cliente HTTP en el frontend (wrapper de `fetch` o axios) que añada automáticamente el header `Authorization: Token <token>` a cada request autenticada
- [ ] Probar login desde el frontend real (no consola) contra la API en local
- [ ] Listar gastos en una tabla simple (sin estilos aún)
- [ ] Formulario para crear gasto
- [ ] Formulario para editar gasto
- [ ] Botón eliminar gasto
- [ ] Manejo básico de errores (mostrar mensaje si el token expira o falla el login)
- [ ] Aplicar estilos mínimos decentes

## Fase 4 — Desplegar el frontend

- [ ] Elegir hosting (Vercel o Netlify)
- [ ] Configurar variable de entorno de producción apuntando a la API de Render
- [ ] Deploy
- [ ] Probar el flujo completo login → crear gasto → ver gasto, en producción real

## Fase 5 — Playwright (E2E)

- [ ] Instalar Playwright en el proyecto frontend
- [ ] Test: login con credenciales válidas lleva al dashboard
- [ ] Test: login con credenciales inválidas muestra error
- [ ] Test: crear un gasto y verificar que aparece en la lista
- [ ] Test: editar un gasto y verificar que se actualiza
- [ ] Test: eliminar un gasto y verificar que desaparece
- [ ] Test: usuario sin sesión es redirigido a login
- [ ] Ejecutar la suite completa y capturar screenshot/reporte de Playwright para el portfolio

## Fase 6 — Portfolio y candidaturas (en paralelo, no al final)

- [ ] Actualizar README: mencionar explícitamente los tests de API (pytest) y E2E (Playwright)
- [ ] Captura o GIF corto del frontend funcionando, para el README
- [ ] Actualizar LinkedIn con el enfoque QA full stack
- [ ] Empezar a aplicar a posiciones ya, sin esperar a que Fase 5 esté terminada

## Fase 7 — Opcional: migración a JWT

*(solo después de tener todo lo demás desplegado y con tests verdes)*

- [ ] Investigar `djangorestframework-simplejwt`
- [ ] Implementar endpoints de login/refresh con JWT
- [ ] Actualizar el cliente HTTP del frontend para usar `Bearer <token>` y manejar el refresh
- [ ] Actualizar tests de pytest afectados por el cambio de auth
