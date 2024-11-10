# Proyecto131-ia_NIMGame

# Modelo Matemático del Juego de Nim (Un Montón)

## Variables y Parámetros
- $N$: Número total de palitos en el montón al inicio del turno.
- $p$: Número de palitos que el jugador decide quitar, donde $p \in \{1,2,3\}$ y $p \leq N$.
- $q$: Número de palitos que la IA decide quitar, donde $q \in \{1,2,3\}$ y $q \leq N$ después del turno del jugador.

## Estados del Juego
Estado del montón después del turno del jugador:
$N' = N - p$

Estado del montón después del turno de la IA:
$N'' = N' - q = N - p - q$

## Condiciones de Fin del Juego
El juego termina cuando el montón está vacío, es decir:
$N \leq 0$

El jugador que hace que $N = 0$ pierde.

## Posiciones Ganadoras y Perdedoras
Para determinar una estrategia óptima, podemos clasificar los estados del juego (valores de $N$) en:

- Posición perdedora: Si $N$ es múltiplo de 4 (es decir, $N \bmod 4 = 0$), el jugador que tiene el turno está en una posición perdedora si su oponente juega óptimamente.
- Posición ganadora: Si $N \bmod 4 \neq 0$, el jugador que tiene el turno está en una posición ganadora y puede forzar a su oponente a una posición perdedora.

## Estrategia Óptima
La estrategia óptima para la IA se calcula así:

Si $N \bmod 4 \neq 0$ (posición ganadora para la IA):
$q = N \bmod 4$

Esto garantiza que el estado resultante sea $N - q = 4k$, donde $k$ es un entero positivo.

Si $N \bmod 4 = 0$ (posición perdedora para la IA):
La IA elige aleatoriamente $q \in \{1,2,3\}$

## Resumen del Modelo Matemático
El modelo para la IA se puede expresar como:

$q = \begin{cases} N \bmod (M + 1) & \text{si } N \bmod (M + 1) \neq 0 \\ \text{valor aleatorio en } \{1,2,.....,M\}, & \text{si } N \bmod (M + 1) = 0 \end{cases}$
