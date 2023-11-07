;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hangmans) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp")) #f)))
;;hang_man
;;设计一个函数通过不同的部分来绘制不同的形状
(define (draw-next-part part)
  (cond
    [(symbol=? part 'right-leg) (draw-solid-line (make-posn 10 10) (make-posn 40 10) 'red)]
    [(symbol=? part 'left-leg) (draw-solid-line (make-posn 10 20) (make-posn 40 20) 'red)]
    [(symbol=? part 'right-arm) (draw-solid-line (make-posn 10 30) (make-posn 40 30) 'red)]
    [(symbol=? part 'left-arm) (draw-solid-line (make-posn 10 40) (make-posn 40 40) 'red)]
    [else (draw-solid-line (make-posn 10 60) (make-posn 40 60) 'red)]))
;;设计一个字母结构体
(define-struct word (a b c))
;;define word word->word
;;设计一个猜单词判断逻辑函数
(define (reveal chosen status guess)
  (cond
    [(symbol=? guess (word-a chosen)) (make-word guess (word-b status) (word-c status))]
    [(symbol=? guess (word-b chosen)) (make-word (word-a status) guess (word-c status))]
    [(symbol=? guess (word-c chosen)) (make-word (word-a status) (word-b status) guess)]
    [else status]))

(start 300 300)
;;(draw-next-part 'dd)
;;(reveal (make-word 't 'e 'a) (make-word '_ 'e '_) 'u)
(hangman make-word reveal draw-next-part)