### __Exercise 1.2__: Translate the ollowing expression into prefix form:

$$
\frac{5 + 4 + (2 - (3 - (6 + 4 / 5)))}{3(6 - 2)(2 - 7)}
$$

#### __Answer:__

```lisp
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5)))))
   (* 3 (- 6 2) (- 2 7)))
```

Which evaluates to 

$$
- \frac{37}{150}
$$

### __Exercise 1.3__: Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.

#### __Answer:__

First we define a procedure that returns the sum of squares of two entries _x_ and _y_, and another that returns the larger between two numbers.

```lisp
(define (squares-sum x y)
    (+ (* x x)
       (* y y)
    )
)

(define (>= x y)
    (or (> x y) (= x y))
)

(define (max x y)
    (if (>= x y) x y)
)
```

Given three numbers _a_, _b_ and _c_, the requested procedure (which we will call _f_) can be applied to _a_ and _b_, _b_ and _c_ or _a_ and _c_ depending on their ordering. The first case happens if $a \geq b \geq c$ or $b \geq a \geq c$; the second if $b \geq c \geq a$ or $c \geq b \geq a$; the third if $a \geq c \geq b$ or $c \geq a \geq b$. Writing it with code, we have the following procedure:

```lisp
(define (f a b c)
    (cond ((or (and (= (max a b) a) (= (max b c) b)) 
               (and (= (max a b) b) (= (max a c) a))) 
           (squares-sum a b))
          ((or (and (= (max b c) b) (= (max a c) c))
               (and (= (max b c) c) (= (max b a) b)))
           (squares-sum b c))
          ((or (and (= (max a c) a) (= (max c b) c))
               (and (= (max c a) c) (= (max a b) a)))
           (squares-sum a c)))
)
```

### __Exercise 1.4__: Observe that our model of evaluation allows for combinations whose operators are compound expressions. Use this observation to describe the behavior of the following procedure:

```lisp
(define (a-plus-abs-b a b)
    ((if (> b 0) + -) a b))
```

#### __Answer:__

The evaluation model for compound procedures is as follows:

```
To apply a compound procedure to arguments, evaluate the body of the procedure with each formal parameter replaced by the corresponding argument.
```

By applying the procedure

```lisp
(a-plus-abs-b a b)
```
the value of _b_ will be used to evaluate the conditional expression

```lisp
(if (> b 0) + -)
```
So, if we have $b > 0$, then the procedure will first be evaluated to

```lisp
(+ a b)
```

Otherwise, if $b \leq 0$, we would have

```lisp
(- a b)
```

which would be simply the sum of _a_ with the absolute value of _b_. Finally, the final value would be returned by reducting the expression.


### __Exercise 1.5__: Ben Bitdiddle has invented a test to determine whether the interpreter he is faced with is using applicative-order evaluation or normal-order evaluation. He defines the following two proceduers:

```lisp
(define (p) (p))
(define (test x y)
    (if (= x 0) 0 y))
```

Then he evaluates the expression

```lisp
(test 0 (p))
```

What behavior will Ben observe with an interpreter that uses applicative-order evaluation? What behavior will he observe with an interpreter that uses normal-order evaluation? Explain our answer. (Assume that the evaluation rule for the special form _if_ is the same whether the interpreter is using normal or applicative order: The predicate expression is evaluated first, and the result determines whether to evaluate the consequent or the alternative expression.)

#### __Answer:__

A interpreter that uses applicative-order evaluation will first evaluate the operator and operands and then apply the resulting procedure to the resulting arguments. The evaluation will start with

```lisp
(test 0 (p))
```

and evaluating first the operator, it will result in

```lisp
((if (= x 0) 0 (p)))
```

The expression _x_ will be evaluated into _0_, but _(p)_ will start an infinite recursion and the program will crash due to stack overflow.

If on the other hand the interpreter uses normal-order evaluation, it will only evaluate the operands when necessary, therefore first it substitutes operand expressions for parameters until it obtains an expression involving only primitive operators, and then it will perform the evaluations. This means that after substituting _test_, it will evaluate the conditional, verifying that _x_ is equal to _0_, returning _0_.

### __Exercise 1.6__: Alyssa P. Hacker doesn't see why _if_ needs to be provided as a special form. "Why can't i just define it as an ordinary procedure in terms of _cond_?" she asks. Alyssa's friend Eva Lu Ator claims this can indeed be done, and she defines a new version of _if_:

```lisp
(define (new-if predicate then-clause else-clause)
    (cond (predicate then-clause)
          (else else-clause)))
```

Eva demonstrates the program for Alyssa:

```
(new-if (= 2 3) 0 5)
5
(new-if (= 1 1) 0 5)
9
```

Delighted, Alyssa uses new-if to rewrite the square-root program:

```lisp
(define (sqrt-iter guess x)
   (new-if (good-enough? guess x)
           guess
           (sqrt-iter (improve guess x) x)))
```

What happens when alyssa attempts to use this to compute square roots? Explain.

#### __Answer:__

The procedure _new-if_ will be evaluated as a normal function, following the evaluation logic for normal procedures where, in the case of an interpreter that uses applicative-order evaluation, will first evaluate each operand and then substitute the final expressions into the operation. This will result in an infinite recursion due to the fact that one of the arguments is another call to _new-if_. 

What if it uses normal-order evaluation?

The _if_ statement, as a special form, will following a specific evaluation logic that avoids infinite recursion and stack overflow.

### __Exercise 1.7__: The _good-enough?_ test used in computing square roots will not be very effective for finding the square roots of very small numbers. Also, in real computers, arithmetic operations are almost always perormed with limited precision. This makes our test inadequate for very large numbers. Explain these statements, with examples showing how the test fails for small and large numbers. An alternative strategy for implementing _good-enough?_ is to watch how _guess_ changes from one iteration to the next and to stop when the chage is a very small fraction of the guess. Design a square-root procedure that uses this kind of end test. Does this work better or small and large numbers?

#### __Answer:__

__Passe para o ingl??s depois.__

Considere $x = 10^{-10}$. A raiz quadrada de $x$ ?? $y = 10^{-5}$. Se tomarmos um valor de chute $z > y$ qualquer, a tend??ncia do algoritmo ?? que ele convirja para o valor $y$ conforme tira-se a m??dia entre $z$ e $x / z$ que ?? bastante pequeno. Todavia, o erro ?? calculado entre $x$ e $z^2$, e por serem valores pequenos, devido ao produto $z \cdot z$ muito rapidamente veremos esse erro menor que o _threshold_ fixado na fun????o _good-enough?_, ainda que o valor de $z$ esteja distante do valor real $y$.

Para valores muito grandes, digamos $x = 2 \cdot 10^{50}$ acontece o problema contr??rio, em que o erro ser?? sempre um valor de uma ordem de grandeza muito superior ao valor de thershold estipulado. Para esse valor de $x$, por exemplo, na itera????o de n??mero $i = 150$ ter??amos um valor de erro na ordem de grandeza de $10^{34}$. Se representarmos as tentativas $z$ na forma $m.n \times 10^p$, onde $p$ ?? um natural, $m$ ?? a parte inteira e $n$ a parte fracion??ria do n??mero multiplicando a pot??ncia de $10$, pode ser poss??vel que o sistema n??o consiga representar o valor mais pr??ximo da raiz $y$ e, com isso, o programa nunca termine pois a maior representa????o num??rica poss??vel tem como resultado um erro excessivamente grande.


### __Exercise 1.8__: Newton's method for cube roots is based on the fact that if _y_ is an approximation to the cube root of _x_, then a better approximation is given by the value $(x/y^2 + 2y)/3$. Use this formula to implement a cube-root procedure analogous to the square-root procedure. 

#### __Answer:__

```lisp
(define (cubert-iter guess x)
    (if (good-enough? guess x)
        guess
        (cubert-iter (improve guess x) x)))

(define (good-enough? guess x)
    (< (abs (- (cube guess) x)) 0.001))

(define (improve guess x)
    (/ (+ (/ x (square guess))
          (* 2 guess))
       3))

(define (cube x)
    (* (* x x) 
        x))

(define (square x)
    (* x x))
```

###__Exercise 1.9__: Each of the following two procedures defines a method for adding two positive integers in terms of the procedures _inc_, which increments its argument by _1_, and _dec_, which decrements its argument by _1_. Using the substitution model, illustrate the process generated by each procedure in evaluating _(+ 4 5)_. Are these processes iterative or recursive?

```lisp
(define (+ a b)
    (if (= a 0) b (inc (+ (dec a) b))))
(define (+ a b)
    (if (= a 0) b (+ (dec a) (inc b))))
```

#### __Answer:__

First case

```
(+ 4 5)
(inc (+ 3 5))
(inc (inc (+ 2 5)))
(inc (inc (inc (+ 1 5))))
(inc (inc (inc (inc (+ 0 5)))))
(inc (inc (inc (inc 5))))
(inc (inc (inc 6)))
(inc (inc 7))
(inc 8)
9
``` 

Second case

```
(+ 4 5)
(+ 3 6)
(+ 2 7)
(+ 1 8)
(+ 0 9)
9
```

The first procedure generates a recursive proccess, since the interpreter needs to keep a stack of _inc_ operations until the procedure returns a number upon which the increments will be applied. The second proccess is an iterative one, at each function call the state variables are modified and passed on.

### __Exercise 1.10:__ The following procedure computes a mathematical function called Ackermann's function.

```lisp
(define (A x y)
    (cond ((= y 0) 0)
          ((= x 0) (* 2 y))
          ((= y 1) 2)
          (else (A (- x 1) (A x (- y 1))))))
```

__What are the values of the following expressions?__

```
(A 1 10)
(A 2 4)
(A 3 3)
```

__Consider the following procedures, where _A_ is the procedure defined above:__

```lisp
(define (f n) (A 0 n))
(define (g n) (A 1 n))
(define (h n) (A 2 n))
(define (k n) (* 5 n n))
``` 

__Give concise mathematical definitions for the functions computed by the procedures _f_, _g_, and _h_ for positive integer values of _n_. For example, _(k n)_ computes $5n^2$.__

#### __Answer:__


