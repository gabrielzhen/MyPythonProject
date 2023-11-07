;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |1500|) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp")) #f)))
(define-struct parent (children name date eyes))
(define Gustav (make-parent empty 'Gustav 1988 'brown))
(define F&E (list Gustav))
(define Adam (make-parent empty 'Adam 1950 'yellow))
(define Dave (make-parent empty 'Dave 1955 'black))
(define Eva (make-parent F&E 'Eva 1955 'blue))
(define Fred (make-parent F&E 'Fred 1966 'pink))
(define C&E (list Adam Dave Eva))
(define Carl (make-parent C&E 'Carl 1955 'green))
(define Bettiua (make-parent C&E 'Bettiua 1966 'green))


;;blue-eye  parent boolean
(define (blue-eye a-parent)
  (cond
    [(symbol=? (parent-eyes a-parent) 'blue) true]
    [else (child-eye (parent-children a-parent ))]))

(define (child-eye a-list)
  (cond
    [(empty? a-list) false]
    [else
     (cond
       [(blue-eye (first a-list)) true]
       [else (child-eye (rest a-list))])]))

(blue-eye Gustav)