;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |1622|) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp")) #f)))
(define-struct files (fi s l))
(define-struct folders (fo l))

(define hang (make-files 'hang 8 empty))
(define draw (make-files 'draw 2 empty))

(define read (make-files 'read 19 empty))
(define code (make-folders 'code (list hang draw)))
(define docs (make-folders 'code (list read)))
(define part1 (make-files 'part1 99 empty))
(define part2 (make-files 'part2 52 empty))
(define part3 (make-files 'part3 17 empty))
(define rdme (make-files 'read 10 empty))

(define libs (make-folders 'libs (list code docs)))
(define text (make-folders 'text (list part1 part1 part1)))

(define ts (make-folders 'ts (list libs text rdme)))

(define (how-many li)
  (cond
    [(empty? li) 0]
    [(files? li) 1]
    [else (how-many-f (folders-l li))]))

(define (how-many-f li)
  (cond
    [(empty? li) 0]
    [(files? (first li)) (+ 1 (how-many-f (rest li)))]
    [else (+ (how-many (first li)) (how-many-f (rest li)))]))

;(how-many ts)
(files- ts)