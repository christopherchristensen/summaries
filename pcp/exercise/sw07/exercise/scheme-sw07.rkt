;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname scheme-sw07) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
; ------- AUFGABE 2 ------- ;

(define (fib n)
  (cond
    ((or (= n 0) (= n 1)) n)
    (else (+ (fib (- n 1))
             (fib (- n 2))))))
; --- a.)


;(define (akku-fib n)
;  )

; --- b.)
; Viel performanter, siehe Beispiel (fib 30) und (akku-fib 30)


; ------- AUFGABE 3 ------- ;
;
; --- a.) 43 und 2
; --- b.) Die Reihenfolge der Auswertung ist anders (let* von links nach rechts)


; ------- AUFGABE 4 ------- ;
;
(define x 1)
(define y 5)

((lambda (x y)
   (+ (* 2 x) y))
 y x) ; 

; --- a.) 11

((lambda (a b)
   (+ (* 2 x) y))
 y x)

; --- a.) 7
; --- b.) x wird y und y wird x zugeordnet. Bei der zweiten Berechnung werden die Parameter ignoriert

; ------- AUFGABE 5 ------- ;
;
; Mit einem Lambda Ausdruck
(define a-list (list (list 1 2 3) (list 1 2) (list 1 2 3 4)))

((lambda (b-list)
   (list
    (cons 0 (first b-list))
    (cons 0 (first (rest b-list)))
    (cons 0 (first (rest (rest b-list))))
    ))
 a-list)

; Rekursive Funktion wäre besser, geht aber nicht mit Lambda

(map (lambda (n) (cons 0 n )) a-list)

; ------- AUFGABE 6 ------- ;

(define rect-calc-list
  (list (lambda (a b) (* a b))
        (lambda (a b) (* 2 (+ a b)))))

(define (calc-a-list f a b)
  (begin
    (display ((first rect-calc-list) a b)) (newline) ; Erste Funktion
    (display ((first (rest rect-calc-list)) a b)) (newline) ; Zweite Funktion
    (display "finished")))

; Funktioniert nur 