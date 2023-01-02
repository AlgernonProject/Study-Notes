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