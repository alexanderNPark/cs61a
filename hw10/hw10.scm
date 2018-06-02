(define (accumulate combiner start n term)
  (if (= n 0)
      start
   (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
 (define (helper i so-far)
  (if (= n i) (combiner so-far (term i))
   (helper (+ i 1) (combiner so-far (term i) ))
  )
 )
 (helper 1 start)
)

(define-macro (list-of expr for var in seq if filter-fn)
 `(map (lambda (,var) ,expr) (filter (lambda (,var) ,filter-fn) ,seq)
))