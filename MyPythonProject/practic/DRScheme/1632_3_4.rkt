;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 1632_3_4) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp")) #f)))
(define-struct files (name size content))
(define-struct dirs (name dirs files))
;; files: 
(define hang (make-files 'hang 8 empty))
(define draw (make-files 'draw 2 empty))
(define read (make-files 'read! 19 empty))
(define one  (make-files 'part1 99 empty))
(define two  (make-files 'part2 52 empty))
(define thre (make-files 'part3 17 empty))
(define rdme (make-files 'read 10 empty))

;; directories: 
(define Code (make-dirs 'Code '() (list hang draw)))
(define Docs (make-dirs 'Docs '() (list read)))
(define Libs (make-dirs 'Libs (list Code Docs) '()))
(define Text (make-dirs 'Text '() (list one two thre)))
(define Top  (make-dirs 'TS (list Text Libs) (list rdme)))

(define (how-many a-dir)
  (+ (how-many-in-dir-list (dirs-dirs a-dir)) 
     (how-many-in-file-list (dirs-files a-dir))))

(define (how-many-in-dir-list dirs)
  (cond
    [(empty? dirs) 0]
    [else (+ (how-many (first dirs)) (how-many-in-dir-list (rest dirs)))]))

(define (how-many-in-file-list files)
  (cond
    [(empty? files) 0]
    [else (add1 (how-many-in-file-list (rest files)))]))

;(how-many Top)


(define (find? d f)
   (or (find-dirs (dirs-dirs d) f) (find-files (dirs-files d) f)))

(define (find-dirs l f)
  (cond
    [(empty? l) false]
    [else (or (find? (first l) f) (find-dirs (rest l) f))]))

(define (find-files l f)
  (cond
    [(empty? l) false]
    [(symbol=? f (files-name (first l))) true]
    [else (find-files (rest l) f)]))

;(find? Code 'hang)

