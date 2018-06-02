(define (find s predicate)
 (cond
  ((null? s) #f)
  ((predicate (car s)) (car s))
  (else (find (cdr-stream s) predicate))
 )
)

(define (scale-stream s k)
 (cond
  ((null? s) nil)
  (else (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k)))
 )
)

(define (has-cycle s)

   (define (temp-cycle new old)
    (cond
     ((null? new) #f)
     ((find old (lambda (x) (equal? x new))) #t)
     (else (temp-cycle (cdr-stream new) (cons-stream new old)))
    )
  )

 (temp-cycle (cdr-stream s)  (cons-stream s nil))

)
(define (has-cycle-constant s)

)
