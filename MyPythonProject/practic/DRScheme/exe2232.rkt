;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname exe2232) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp")) #f)))
;;模型 define finde-mes string list ->number
(define-struct telep (name telephone))
(define n-list (list (make-telep "a" 123) (make-telep "b" 456) (make-telep "c" 146)))

(define (finde-mes x n-list)
  (cond
    [(empty? n-list) 999]
    [(string=? x (telep-name (first n-list))) (telep-telephone (first n-list))]
    [else (finde-mes x (rest n-list))]))

;(finde-mes "d" n-list)


;;视图
;define text
(define tx (make-text "enter name"))
;define message
(define me (make-message "waiting"))
;reback function
(define (echo-mes e)
  (draw-message me (number->string (finde-mes (text-contents tx) n-list))))
;draw window
(create-window
 (list (list tx me)
 (list (make-button "check" echo-mes))))
