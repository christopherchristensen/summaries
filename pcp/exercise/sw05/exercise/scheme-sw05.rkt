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
;     Stellt man den Fall > temperatur 15 zuoberst hin, wertet die Funktion
;     alles über 15 als "mittel" aus.
;     Scheme arbeitet die Fälle der Reihe von oben nach unten nach durch.
;     Aus diesem Grund ist die Reihenfolge durchaus wichtig.
;     Kann aber in einzelnen Fällen egal sein.
(define (temperatur-evaluator temperatur)  
  (cond
    ((> temperatur 15) "mittel")
    ((> temperatur 25) "warm")
    ((> temperatur 35) "heiss")
    (else "kalt")))

; b.) In diesem Fall kommt es insofern darauf an, dass eine Zahl, die durch
;     3 und 2 teilbar sind, jeweils nur einen der beiden Teiler ausgibt.
(define (teilbarkeit-rechner zahl)
  (cond
    ((zero? (remainder zahl 3)) "durch 3 teilbar")
    ((zero? (remainder zahl 2)) "durch 2 teilbar")
    (else "weder durch 2 noch durch 3 teilbar")))

; --- AUFGABE 6

; a.) 1. Klausel versichert, dass die Eingabe eine Zahl vor weiterer Evaluation
;     2. Klausel versichert, dass Eingabe eine Zahl grösser als 0 ist

; b.) Ist die Eingabe keine Zahl wirft die 2. Klausel (nun die 1.) einen Fehler
(define (toll total-weight)
  (cond
    ((<= total-weight 0) "Zahl muss größer 0 sein!")
    ((not (number? total-weight)) "Eingabe muss Zahl sein!")
    ((<= total-weight 1000) 20)
    ((<= total-weight 2000) 30)
    ((<= total-weight 5000) 50)
    ((<= total-weight 10000) 100)
    (else 250)))

; c.) Wo ein Switch-ähnliches Szenario gefragt ist (mit eingeschränkten Wertebereich)
(define (switch-case number)
  (cond
    ((= number 0) "You entered the number 0")
    ((= number 1) "You entered the number 1")
    ((= number 2) "You entered the number 2")
    (else "I'm sorry, I can only count to 2")))

; --- AUFGABE 7

; a.) Nein, a und b sind nicht definiert (Lazy Evaluation)
; b.)

(define (task7 a b) (*
 (cond ((> a b) a)
       ((< a b) b)
       (else -1))
 (+ a 1)
))

; --- AUFGABE 8

(define (distance x y)
  (sqrt (+ (* x x) (* y y))))

; --- AUFGABE 9

(define-struct human (age gender obershenkelknookslength))

(define man (make-human 30 "man" 30))
(define woman (make-human 50 "woman" 30))

(define (b-length h)
  (cond
    ((string=? (bö(human-gender h) "man") (- (+ 69.089 (* 2.238 (human-obershenkelknookslength h))) (* 0.06 (human-age h))))
    ((string=? (human-gender h) "woman") (- (+ 61.412 (* 2.317 (human-obershenkelknookslength h))) (* 0.06 (human-age h))))
    (else "wrong parameters")))

    