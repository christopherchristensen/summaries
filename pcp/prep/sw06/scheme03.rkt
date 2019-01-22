;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname scheme03) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define mylist (list 'a 'b 'c 'd 'e 'f 'g))
(define otherlist (list 'ab 'cd 'de 'ef))
(define cheeselist (list 'cheese1 'cheese2 'cheese3 'cheese4))
(define hatlist '(hat1 tophat hat3))

(define numlist-1 (list 1 2 3 4 5 6 7 8 9))
(define numlist-2 (list 9 8 7 6 5 4 3 2 1))
(define numlist-3 (list 1 3 5 7 9 2 4 6 8))
(define numlist-4 (list 2 4 6 8 1 3 5 7 9))
(define numlist-5 (list 9 7 5 3 1 8 6 4 2))
(define numlist-6 (list 8 6 4 2 9 7 5 3 1))

(define negnums-1 (list -1 2 -3 4 -5 6 -7 8 -9))
(define negnums-2 (list 1 -2 3 -4 5 -6 7 -8 9))

(define (sum a-list)
  (cond
    [(empty? a-list) 0] ;Rekursionsbasis
    [else (+ (first a-list) (sum (rest a-list)))]
    )
  )

(define (listdouble a-list)
  (cond
    [(empty? a-list) '()]
    [(not (number? (first a-list))) a-list]
    [else (cons (* 2 (first a-list)) (listdouble (rest a-list)))]
    ))

(define (sorted-insert value a-list)
  (cond
    [(empty? a-list) '()]
    [(not (number? (first a-list))) a-list]
    [(>= value (first a-list)) (sorted-insert value (rest a-list))]
    [else (append value a-list)]
    ))



(define (max-st a-list)
  (cond
    [(empty? (rest a-list)) (first a-list)]
    [else
     (cond
       [(> (first a-list) (max-st (rest a-list))) (first a-list)]
       [else (max-st (rest a-list))]
       )
     ]
    ))

(define (squarenumber? value)
  (integer? (sqrt value)))

(begin
  (display "type your name here: ")
  (let* ([a (read)])
    (cond
      [(empty? a) empty]
      [else (begin
              (display "Hi, ")
              (display a)
              (display "! Welcome to Scheme \\(^L^)/"))
            ]
      )
    )
  )
