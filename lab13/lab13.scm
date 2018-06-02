; Q1
(define (compose-all funcs)
 (cond
  ((null? funcs) (lambda (x) x))
  (else (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)) ))
 )
)

; Q2
(define (tail-replicate x n)

 (define (roll rest index)
  (cond
   ((= index 0) rest)
   (else (roll (cons x rest) (- index 1)))
  )
 )

 (roll nil n)

)