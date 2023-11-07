;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |1712|) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp")) #f)))
;;define cross list list->list

(define (cross la lb)
  (cond
    [(empty? la)
       empty]
    [else
     (append (m-list (first la) lb) (cross (rest la) lb))]))

(define (m-list la lb)
  (cond
    [(empty? lb) empty]
    [else (cons (list la (first lb)) (m-list la (rest lb)))]))

(cross (list 'a 'b) (list 1 2 3))