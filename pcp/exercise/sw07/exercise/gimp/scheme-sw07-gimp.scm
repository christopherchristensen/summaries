; GIMP Skript das ein konfigurierbares Gitternetz im GIMP zeichnet
; Im GIMP und im Menu registrieren
(script-fu-register 
 "script-fu-grid-lines" ; Funktionsname
 "New gridlines"	; Menu Punkt
 "Illustrates the structure of a GIMP script" ; Beschreibung
 "Roger Diehl"          ; Autor
 "2018, HSLU - I"     ; Copyright Notiz
 "October 2018"         ; Erstellungsdatum
 ""                     ; Bild Typ des Skript - "" heisst, es muss kein Bild geladen sein, für IMG "RGB"
 ; aktuelle Parameter von script-fu-grid-lines
 SF-ADJUSTMENT "Image width" '(200 10 10000 1 1 0 1) ; drawable_width - default 200
 SF-ADJUSTMENT "Image height" '(200 10 10000 1 1 0 1); drawable_height - default 200
 SF-ADJUSTMENT "Spacing" '(20 2 100 1 1 0 1)         ; spacing - default 20
 SF-BRUSH "Brush" '("Circle (01)" 100.0 1 0)         ; brush - default Circle (01)
 SF-COLOR "Background" '(255 255 255)                ; background color - default black
 SF-COLOR "Foreground" '(0 0 0)                      ; foreground color - default white
 SF-TOGGLE "Transparent Layer" FALSE                 ; transparent - default FALSE
 SF-TOGGLE "Horizontal lines" TRUE                   ; horizontal - default TRUE
 SF-TOGGLE "Vertical lines" FALSE                    ; vertical - default FALSE
 SF-TOGGLE "Dashed lines" FALSE                      ; dashed - default FALSE
 )
(script-fu-menu-register "script-fu-grid-lines"
                         "<Image>/File/Create/Gridlines")

; Das eigentliche Skript
(define (script-fu-grid-lines drawable_width drawable_height spacing brush background foreground transparent horizontal vertical dashed)
  
  (gimp-context-push)
  (let*(
        ; Grundeinstellungen - Farbe, Breite, Höhe, Ebene...
        (color 0)
        (image (car(gimp-image-new drawable_width drawable_height RGB)))
        (layer (car(gimp-layer-new image drawable_width drawable_height RGBA-IMAGE "grid-layer" 100 NORMAL-MODE)))
        (layer_width (car(gimp-drawable-width layer)))
        (layer_height (car(gimp-drawable-height layer)))
        ; Anfangs- und Endpunkt einer Linie definieren x1, y1, x2, y2
        (point (cons-array 4 'double))
        (invert FALSE)
        )
    ; Gimp Kontext sezten - Transparenz, Hintergrund, Vordergrund, Pinsel, Füllfarbe, Ebene...
    (if(= transparent TRUE)
       (set! color TRANSPARENT-FILL)
       (set! color BACKGROUND-FILL)
       )
    (gimp-context-set-background background)
    (gimp-context-set-foreground  foreground)
    (gimp-context-set-brush (car brush))
    (gimp-drawable-fill layer color)
    (gimp-image-add-layer image layer -1)
    
    ; Demo zum Zeichnen einer Linie
    (define (draw_line x1 y1 x2 y2)
      ; Variablen x1, y1, x2, y2 den Anfangs- und Endpunkten der Linie zuordnen
      (aset point 0 x1)
      (aset point 1 y1)
      (aset point 2 x2)
      (aset point 3 y2)
      ; Linie zeichnen
      (gimp-paintbrush-default layer 4 point)
      )
    
    
    
    ; ab hier die Gitterlinien-Funktionen...
    ; ------------------------------------------------------

    ; --- DEFINITIONEN ---
    
    ; Funktion um eine horizontale Linie zu zeichnen
    (define (draw_horizontal_line y)
      (if 
       (< y layer_height) ; bis y gleich gross wie layer_height (oben definiert als drawable height)
       (begin 
         (draw_line 0 y layer_width y) ; Verwende Funktion draw_line (x1 bleibt 0)
         (draw_horizontal_line (+ y spacing)) ; Incrementiere y
         )))

    ; Funktion um eine vertikale Linie zu zeichnen
    ; Nach gleichem Prinzip wie oben
    (define (draw_verticale_line x)
      (if
       (< x layer_width) 
       (begin 
         (draw_line x 0 x layer_height) ; (y1 bleibt 0)
         (draw_verticale_line (+ x spacing)) ; incrementiere
         )))

    ; Funktion um eine gestrichelte horizontale Linie zu zeichnen
    (define (draw_dashed_horizontal_line x y) (if
      (< y layer_height) ; solange y kleiner als layer height (vordefiniert)
      (begin
        (if 
         (<= x layer_width) ; x kleiner gleich vordefinierte max width??
         (begin
           (draw_line x y (+ x spacing) y)
           (draw_dashed_horizontal_line (+ x (* 2 spacing)) y) ; 
           )
         (draw_dashed_horizontal_line 0 (+ y spacing))
      ))))

    ; Funktion zum Zeichnen einer gestrichelter vertikalen Linie
    (define (draw_dashed_verticale_line y x) (if
      (< x layer_width)
      (begin (if
        (<= y layer_height)
        (begin
          (draw_line x y x (+ y spacing))
          (draw_dashed_verticale_line (+ y (* 2 spacing)) x)
        )
        (draw_dashed_verticale_line 0 (+ x spacing))
      ))
    ))

    ; --- ZEICHNEN ---
    ; Diagonale Linie zeichnen falls weder horizontal noch vertikal angewählt ist
    (cond (
      (and (eq? vertical FALSE) (eq? horizontal FALSE))
      (draw_line spacing spacing (- layer_width spacing) (- layer_height spacing))
    ))

    ; Horizontal ausgezogene Linien zeichnen falls horizontal angewählt ist
    (cond (
      (and (eq? horizontal TRUE) (eq? dashed FALSE))
      (draw_horizontal_line spacing)
    ))

    ; Vertikale ausgezogene Linien zeichnen falls vertikal angewählt ist
    (cond (
      (and (eq? vertical TRUE) (eq? dashed FALSE))
      (draw_verticale_line spacing)
    ))

    ; Horizontal gestrichelte Linien zeichnen falls horizontal und gestrichelt angewählt sind
    (cond (
      (and (eq? horizontal TRUE) (eq? dashed TRUE))
      (draw_dashed_horizontal_line 0 spacing)
    ))

    ; Vertikale gestrichelte Linien zeichnen falls vertikal und gestrichelt angewählt sind
    (cond (
      (and (eq? vertical TRUE) (eq? dashed TRUE))
      (draw_dashed_verticale_line spacing 0)
    ))
    

    ; ------------------------------------------------------
    ; ...Ende der Gitterlinien-Funktionen
    
    ; Bild anzeigen
    (gimp-display-new image)
    (gimp-context-pop)
    (gimp-displays-flush)
    )
  )
