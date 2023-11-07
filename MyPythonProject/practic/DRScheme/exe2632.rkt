;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname exe2632) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp")) #f)))
(define (gcd-structural n m)
  (local ((define (first-divisior-<= i)
	    (cond
	      [(= i 1) 1]
	      [else (cond
		      [(and (= (remainder n i) 0) 
			    (= (remainder m i) 0))
		       i]
		      [else (first-divisior-<= (- i 1))])])))
    (first-divisior-<= (min m n))))
(define (gcd-generative n m)
  (local ((define (clever-gcd larger smaller)
	    (cond
	      [(= smaller 0) larger]
	      [else (clever-gcd smaller (remainder larger smaller))])))
    (clever-gcd (max m n) (min m n))))
(gcd-generative 101135853 45014640)