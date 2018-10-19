;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname scheme-sw05) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; --- AUFGABE 1

; a.) 5
(/ (+ 42 (- 25 (* 3 4))) 11)

; b.) 14
(+ (/ (+ 24 32) 7) (* 3 (- 17 15)))

; c.) 0
(- (/ 34428 38) (- 1103 197))


; --- AUFGABE 2

; a.) 1 : (1 + 1)
; b.) 1 : (1 + 1 : (1 + 1))
; c.) 1 : (1 + 1 : (1 + 1 : (1 + 1)
; Es werden viel weniger Klammern benötigt für die mathematische Notation wegen der "Punkt vor Strich"-Regel!


; --- AUFGABE 3

(define (diagonal-of-rectangle width height)
  (sqrt (+ (* width width) (* height height))))

; --- AUFGABE 4

; a.)

(define (calculate-params a b c)
  (* -1 (* 30 (+ a (- b c)))))

; b.) In dem man die Funktion zuerst vereinfacht und danach in Scheme schreibt

; --- AUFGABE 5

; a.) Nein, denn das verändert in diesem Fall die Semantik.
;     Scheme arbeitet die Fälle der Reihe von oben nach unten nach durch
(define (temperatur-evaluator temperatur)  
  (cond
    ((> temperatur 35) "heiss")
    ((> temperatur 25) "warm")
    ((> temperatur 15) "mittel")
    (else "kalt")))

