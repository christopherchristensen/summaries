;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname scheme-sw06) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define couple (list (cons "Adam" (cons "Eva" empty))
                     (cons "Paul" (cons "Paula" empty))))

(define spec-list (list 1 (list 2 3 (list 5 7) 9)))

; ------- AUFGABE 1 ------- ;
;
; --- a.)
; (rest (first couple))          => (list "Eva"), Rest der ersten Liste
; (first (rest couple))          => (list "Paul" "Paula"), Rest gibt immer eine Liste zurück, das heisst auch wenn der zweite Eintrag bereits eine Liste ist, wird daraus eine weitere Liste erzeugt
; (rest (rest couple))           => '(), Der erste Eintrag der Liste, die sich ergibt aus (rest couple), ist die Liste mit "Paul" und "Paula". Somit ist der Rest eine leere Liste
; (first (first (rest couple)))  => "Paul", Erweiterung der zweiten Eingabe => erstes Element der Liste (list "Paul" "Paula")
; (rest (first (rest couple)))   => (list "Paula"), Rest gibt immer eine Liste zurück. Um Paula als Element zu erhalten muss man diese Eingabe mit (first ...) erweitern.
; (cons? (rest (rest couple)))   => # false, obwohl es sich eigentlich um eine Liste handelt => diese Liste ist jedoch eine leere Liste '()

; --- b.)
; (first (rest (first (rest (rest (first (rest spec-list)))))))


; ------- AUFGABE 2 ------- ;
;
(define (redouble a-list)
(cond ((empty? a-list) empty)
        (else
         (cons (* 2 (first a-list))
               (redouble (rest a-list))))
))

(define (multiply-by factor a-list)
(cond ((empty? a-list) empty)
        (else
         (cons (* factor (first a-list))
               (redouble (rest a-list))))
))



; ------- AUFGABE 3 ------- ;
;
; --- a.)
; Gibt immer das letzte Element der Liste (wenn das letzte Element eine Liste ist, wird diese Liste zurückgegeben)
; Die Listenelemente benötigen die Argumente Liste (oder 'first' und 'rest')???
(define (f liste)
(if (empty? liste)
    empty
    (if (empty? (rest liste))
        (first liste)
        (f (rest liste)))))

; --- b.)
; Gibt immer das grösste Element der Liste zurück (muss deshalb eine Zahl sein!)
(define (g liste)
  (cond
    ((empty? liste) empty)
    ((empty? (rest liste)) (first liste))
    (else
     (if (> (first liste) (g (rest liste)))
         (first liste)
         (g (rest liste))))))

; ------- AUFGABE 4 ------- ;
;
(define (delete item a-list)
  (cond
    ((empty? a-list) empty)                                ; falls Liste leer, leere Liste zurück
    ((eqv? item (first a-list)) (rest a-list))             ; falls item gleich erstes Listenelement, Rest der Liste zurück
    (else                                                  ;
     (cons (first a-list) (delete item (rest a-list))))))


; ------- AUFGABE 5 ------- ;
;
(define (contains? item a-list)
  (cond
    ((empty? a-list) #f)
    ((eqv? item (first a-list)) #t)
    (else
     (contains? item (rest a-list)))))


; ------- AUFGABE 6 ------- ;
;
(define (list-filter rel-op a-list value)
  (cond
    [(empty? a-list) empty]
    [else
     (cond
       [(rel-op (first a-list) value)
        (cons (first a-list)
              (list-filter rel-op (rest a-list) value))]
       [else (list-filter rel-op (rest a-list) value)])
]))
; --- a.) Geht nicht mit Relationsoperatoren
; (list-filter eqv? '(a b c) 'b) würde gehen

; --- b.) Geht auch nicht mit Relationsoperatoren
; (list-filter eqv? (list #\a #\b #\c) #\a)

; --- c.) Geht
; (list-filter eqv? (list "A" "B" "C") "A")
; (list-filter eqv? (list "A" "B" "C") (list "B" "C")) => leere Liste?


; ------- AUFGABE 7 ------- ;
;
(define (list-filter-divisor a-list divisor)
  (cond
    [(empty? a-list) empty]
    [(= (remainder (first a-list) divisor) 0)
     (cons (first a-list) (list-filter-divisor (rest a-list) divisor))]
    [else (list-filter-divisor (rest a-list) divisor)]))


; ------- AUFGABE 8 ------- ;
;
; Sortieren durch Einfügen
(define (sort-a-list list rel)
  (cond
    
    [(empty? list) empty] ; leere Liste
    
    [(string? (first list)) ; hat String in der Liste
     (cond
       [(rel 1 2) (sort list string<?)]
       [else (sort list string>?)])]
     
    [else (sort list rel)]
                  
))

; Einfügen in sortierter Liste
(define (insert item a-list)
  (cond
    [(empty? a-list) (list item)]
    [(<= item (first a-list)) (cons item a-list)]
    [else (cons (first a-list) (insert item (rest a-list)))]
    ))

; (sort-a-list (list "ape" "cat" "bird") <) => (list "ape" "bird" "cat")
; (sort-a-list (list "ape" "cat" "bird") >) => (list "cat" "bird" "ape")
; (sort-a-list '(1 4 5 2) <)                => (list 1 2 4 5)
; (sort-a-list '(1 4 5 2) >)                => (list 5 4 2 1)

; ------- AUFGABE 9 ------- ;
;
; --- a.)
; Gibt das Vorzeichen einer Zahl zurück (Addition Operator?)
(define (a-op a)
  (cond
    [(>= a 0) +]
    [else -]))

; --- b.)
;
; => abs-a-plus-b
(define (abs-a-plus-b a b)
  (a-add-b-helper
   (abs a) (abs b) (a-op a) (a-op b)
   ))

; Hilfsfunktion
(define (a-add-b-helper a b opA opB)
  (+ (opA a) (opB b)))

; (abs-a-plus-b -1 2)  ; =>  1
; (abs-a-plus-b -1 -2) ; => -3
; (abs-a-plus-b 1 -2)  ; => -1
; (abs-a-plus-b 1 2)   ; =>  3

; --- c.)
;
; => abs-a-op-b
(define (abs-a-op-b op a b)
  (a-op-b-helper
   op (abs a) (abs b) (a-op a) (a-op b)
   ))

; Hilfsfunktion
(define (a-op-b-helper op a b opA opB)
  (op (opA a) (opB b)))

; (abs-a-op-b * -1 2)  ; => -2
; (abs-a-op-b / -1 2)  ; => -0.5
; (abs-a-op-b / -2 1)  ; => -2


