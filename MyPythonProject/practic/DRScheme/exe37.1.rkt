;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname exe37.1) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp")) #f)))
(define chosen-word (random word))
(define status-word ...)
(defin hangman-left '(leftarm rightarm body head leftleg rightleg))

(define (hangman)
  (begin
    (set! chosen-word (random word))
    (set! hangman-left '(leftarm rightarm body head leftleg rightleg)))
  )

(define (reveal-list status-word chosen-word guess)
  (...))

(define (hangman-guess guess)
  (local ((define new-status (reveal-list status-word chosen-word guess)))
    (cond
    [(equal? chosen-word new-status)
     "you win"];;猜对了完整的单词  输出完成
    [(equal? status-word new-status)
     (local ((define next-part (first hangman-left)))
       (begin
         (set! hangman-left (rest hangman-left))
         (cond
           [(empty? hangman-left) (list "the end" chosen-word)]
           [else (list "sorry" next-part status-word)])
       ))];;没有猜对字母
    [else
     (begin
       (set! status-word new-status)
       (list "good guess go on" status-word))];;猜对了字母  继续下一个
    )))