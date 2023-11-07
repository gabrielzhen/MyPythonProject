;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname exe2233) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp")) #f)))
;;模型

;;视图
(define pad '((1 2 3) (4 5 6) (7 8 9) (\# 0 *)))
(define (to-str x) (cond [(symbol? x) (symbol->string x)] [else (number->string x)]))
(define a-mes (make-message "num"))

(define (echo-mes x)
  (local ((define (ce e)
  (draw-message a-mes (to-str x))))
  ce))

(define (mk-bt pad)
   (cond
    [(empty? pad) empty]
    [(list? (first pad)) (cons (mk-bt (first pad)) (mk-bt (rest pad)))]
    [else (cons (make-button (to-str (first pad)) (echo-mes (first pad))) (mk-bt (rest pad)))]))
;(cons (make-button (to-str (first pad)) (echo-mes (first pad))) (mk-bt (rest pad)))

(mk-bt pad)

(create-window
 (cons (list a-mes) (mk-bt pad)))