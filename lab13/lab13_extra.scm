; Q4
(define (rle s)
 (cond
  ((null? s) nil)
  (else

   (define (massCdr one element)
    (cond
     ((null? one) nil)
     (else (if (not (eq? element (car one))) one (massCdr (cdr-stream one) element)))
    )
   )

   (cons-stream (list (car s) (count (car s) s)) (rle (massCdr s (car s))))

  )
 )

)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
 (define (activate start rest)

  (if (or (null? rest) (< n (car rest)))
   (append (append start (list n)) rest)
   (activate (append start (list (car rest))) (cdr rest))
  )

 )
 (activate nil s)
)

; Q6
(define (deep-map fn s)
 (cond
  ((null? s) nil)
  ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
  (else (cons (fn (car s)) (deep-map fn (cdr s))))

 )
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  'YOUR-CODE-HERE
  nil
)

(define (count name s)
 (cond
  ((or (null? s) (not (eq? name (car s)))) 0)
  (else (+ 1 (count name (cdr-stream s))))
 )
)

(define (tally names)
  'YOUR-CODE-HERE
  nil
)