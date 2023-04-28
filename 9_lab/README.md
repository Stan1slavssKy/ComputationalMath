# Лабораторная работа номер 9
## Практикум Демченко. Лабораторная работа №4 - Вариант 3. Задание 7.
### Постановка задачи
Найти решение краевой задачи для одномерного стационарного уравнения теплопроводности

$$\frac{d}{dx}\left[k(x)\frac{du}{dx}\right] - q(x)u = -f(x)$$

в одиннадцати равноудаленных точках отрезка $[0,1]$ с относительной точностью $0,0001$. Отладку программы произвести на модельной задаче с постоянными коэффициентами.


Краевые условия задачи $u(0) = 0;~ u(1) = 1.$
Дополнительные условия в точке разрыва
$$u(x_0 - 0) = u(x_0 + 0)$$
$$k(x_0 - 0)u'_x(x_0 - 0) = k(x_0 + 0)u'_x(x_0 + 0)$$
$$x < x_0 = \frac{1}{\sqrt{2}};~ k(x) = e^{\sin{x}};~ q(x) = 2;~ f(x) = e^x$$
$$x > x_0 = \frac{1}{\sqrt{2}};~ k(x) = 1;~ q(x) = 1;~ f(x) = e^x$$

Модельная задача 
$$x_0 = \frac{1}{\sqrt{2}};~ k(x) = k(x_0);~ q(x) = q(x_0);~ f(x) = f(x_0)$$

### Решение
Для решения задачи используется метод встречных прогонок. Введем на области интегрирования равномерную сетку, выбрав в качестве узлов точки $x_l = lh,~ l = \overline{0,L},~ h = \frac{1}{L}$.

Пусть точка разрыва $x_0$ находится между узлами $l_\alpha$ и $l_\beta$, так что $x_{l_\alpha} \leq x_0 \leq x_{l_\beta},~ l_\beta < L$.

Для постановки разностной задачи в каждом узле сетки $l = \overline{1, l_\alpha-1}$ и $l = \overline{l_\beta + 1, L - 1}$ (т.е индекс $\alpha$ до разрыва, $\beta -$ после). Заменим вторую производную конечноразностным отношением c использованием следующих обозначений

$$k_\alpha(x_l \pm h/2) = k_\alpha(x_{l \pm l/2}) = (k_\alpha)_{l \pm l/2}$$

$$k_\beta(x_l \pm h/2) = k_\beta(x_{l \pm l/2}) = (k_\beta)_{l \pm l/2}$$

$$q_\alpha(x_l) = (q_\alpha)_l;~ f_\alpha(x_l) = (f_\alpha)_l$$

$$q_\beta(x_l) = (q_\beta)_l;~ f_\beta(x_l) = (f_\beta)_l$$

$$\left[\frac{d}{dx}\left(k(x)\frac{du}{dx}\right)\right]_{x = x_l} \approx \frac{(k_\alpha)_{l+1/2} \frac{u_{l+1} - u_l}{h} - (k_\alpha)_{l - 1/2} \frac{u_l - u_{l-1}}{h}}{h},~ l = \overline{1, l_\alpha - 1}$$

$$\left[\frac{d}{dx}\left(k(x)\frac{du}{dx}\right)\right]_{x = x_l} \approx \frac{(k_\beta)_{l+1/2} \frac{u_{l+1} - u_l}{h} - (k_\beta)_{l - 1/2} \frac{u_l - u_{l-1}}{h}}{h},~ l = \overline{l_\beta + 1, L-1}$$

После подстановки этих выражений в дифференциальное уравнение, приходим к системе линейных уравнений порядка $L-3$ относительно $L+1$ неизвестного значения сеточной функции $u_l,~\overline{0,L}:$

$$\frac{(k_\alpha)_{l+1/2}(u_{l+1} - u_l) - (k_\alpha)_{l-1/2}(u_l - u_{l-1})}{h^2} - (q_\alpha)_l u_l = -(f_\alpha)_l,~ l = \overline{1, l_{\alpha} - 1}$$

$$\frac{(k_\beta)_{l+1/2}(u_{l+1} - u_l) - (k_\beta)_{l-1/2}(u_l - u_{l-1})}{h^2} - (q_\beta)_l u_l = -(f_\beta)_l,~ l = \overline{l_\beta + 1, L-1}$$

Добавляя к этой системе краевые условия задачи и условия сопряжения в разрыве, получаем полноценную систему

$$a_l = (k_\alpha)_{l+1/2};~ b_l = -\left[(k_\alpha)_{l+1/2} + (k_\alpha)_{l-1/2} + (q_\alpha)_l h^2\right];~ l = \overline{1, l_\alpha - 1}$$

$$c_l = (k_\alpha)_{l-1/2};~ d_l = -(f_\alpha)_l h^2;~ l = \overline{1, l_\alpha - 1}$$

$$a_l = (k_\beta)_{l+1/2};~ b_l = -\left[(k_\beta)_{l+1/2} + (k_\beta)_{l-1/2} + (q_\beta)_l h^2\right];~ l = \overline{l_\beta + 1, L-1}$$

$$c_l = (k_\beta)_{l-1/2};~ d_l = -(f_\beta)_l h^2;~ l = \overline{l_\beta + 1, L-1}$$

$$\begin{equation*} 
    \begin{cases}
        u_0 = u^0, \\
        a_l u_{l+1} + b_l u_l + c_l u_{l-1} = d_l,~ l = \overline{1, l_\alpha - 1}, \\
        u_{l_\alpha} = u_{l_\beta}, \\
        (k_\alpha)_{l_\alpha}(u_{l_\alpha} - u_{l_\alpha} - 1) = (k_\beta)_{l_\beta} (u_{l_\beta + 1} - u_{l_\beta}), \\
        a_l u_{l+1} + b_l u_l + c_l u_{l-1} = d_l,~ l = \overline{l_\beta + 1, L-1}, \\
        u_L = u^1.
    \end{cases}
\end{equation*}$$

Решаем данную систему. Для начала выражаем из первого уравнения $u_0$ и подставляем во второе. Из последнего выражаем $u_L$ и подставляем в предпоследнее

$$\begin{equation*}
    \begin{cases}
        u_1 = -\frac{a_1}{b_1} u_2 + \frac{d_1 - c_1 u_0}{b_1}\, = \alpha_1 u_2 + \beta_1, \\
        u_{L - 1} = -\frac{c_{L - 1}}{b_{L - 1}}u_{L - 2} + \frac{d_{L - 1} - c_{L - 1} u_L}{b_{L - 1}} = \alpha_{L - 1} u_{L - 2} + \beta_{L - 1}
    \end{cases}
\end{equation*}$$
		
Действуя по аналогии получаем:

$$\begin{equation*}
    \begin{cases}
        u_{l - 1} = \alpha_{l - 1} u_l + \beta_{l - 1},~ l = \overline{1,l_\alpha - 1} \\
        u_{l + 1} = \alpha_{l + 1} u_l + \beta_{l + 1},~ l = \overline{L - 1,l_\beta + 1}
    \end{cases}
\end{equation*}$$

Прогоночные коэффициенты определяются следующим образом:

$$\alpha_l = -\frac{a_l}{b_l + c_l \alpha_{l-1}},$$

$$\beta_l  =  \frac{d_l - c_l \beta_{l-1}}{b_l + c_l \alpha_{l - 1}},~ l = \overline{2, l_\alpha - 1}$$

$$\alpha_l = -\frac{c_l}{b_l + a_l \alpha_{l+1}},$$

$$\beta_l  =  \displaystyle\frac{d_l - a_l \beta_{l+1}}{b_l + a_l \alpha_{l + 1}},~ l = \overline{L - 2, l_\beta + 1}$$

Теперь рассмотрим систему

$$\begin{equation*}
    \begin{cases}
        u_{l_\alpha - 1} = \alpha_{l_\alpha - 1} u_{l_\alpha} + \beta_{l_\alpha - 1}, \\
        u_{l_\alpha} = u_{l_\beta}, \\
        (k_\alpha)_{l_\alpha}(u_{l_\alpha} - u_{l_\alpha - 1}) = (k_\beta)_{l_\beta}(u_{l_\beta + 1} - u_{l_\beta}), \\
        u_{l_\beta  + 1} = \alpha_{l_\beta  + 1} u_{l_\beta}  + \beta_{l_\beta  + 1}.
    \end{cases}
\end{equation*}$$

Решим ее получаем

$$\begin{equation*}
    \begin{cases}
        u_{l_\alpha} = u_{l_\beta} = \displaystyle\frac{(k_\alpha)_{l_\alpha}\beta_{l_\alpha - 1} + (k_\beta)_{l_\beta}\beta_{l_\beta + 1}}{(k_\alpha)_{l_\alpha}(1 - \alpha_{l_\alpha - 1}) + (k_\beta)_{l_\beta} (1 - \alpha_{l_\beta + 1})}, \\
        u_{l_\alpha - 1} = \alpha_{l_\alpha - 1} u_{l_\alpha} + \beta_{l_\alpha - 1}, \\
        u_{l_\beta + 1} = \alpha_{l_\beta + 1} u_{l_\beta} + \beta_{l_\beta + 1}.
    \end{cases}
\end{equation*}$$
