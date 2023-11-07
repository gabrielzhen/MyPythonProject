;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname exe2813) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp") (lib "dir.rkt" "teachpack" "htdp") (lib "gui.rkt" "teachpack" "htdp")) #f)))
(define Graph 
  (list (list 'A (list 'B 'E))
        (list 'B (list 'E 'F))
	(list 'C (list 'D))
	(list 'D empty)
	(list 'E (list 'C 'F))
	(list 'F (list 'D 'G))
	(list 'G empty)))

(define (neighbors a-node a-graph)
  (cond
    ((empty? a-graph) (error 'neighbors "can't happen"))
    (else (cond
	    ((eq? (first (first a-graph)) a-node)
	     (second (first a-graph)))
	    (else (neighbors a-node (rest a-graph)))))))

(define (find-route origination destination g)
  (cond
    [(symbol=? origination destination) (list destination)]
    [else (local
            ((define possible-route (find-route/list (neighbors origination g) destination g)))
            (cond
              [(boolean? possible-route) false]
              [else (cons origination possible-route)]))]))

(define (find-route/list lo d g)
  (cond
    [(empty? lo) false]
    [else (local
            ((define possible-route (find-route (first lo) d g)))
            (cond
              [(boolean? possible-route) (find-route/list (rest lo) d g)]
              [else possible-route]))]))


(find-route 'C 'G Graph)