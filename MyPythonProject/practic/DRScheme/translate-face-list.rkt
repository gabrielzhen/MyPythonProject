;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname translate-face-list) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp") (lib "arrow.rkt" "teachpack" "htdp")) #f)))
;;创建一个脸图形列表
(define-struct circle (posn banjin color))
(define-struct trangle (posn lang width color))
(define face
  (cons (make-circle (make-posn 50 50) 40 'red)
        (cons (make-trangle (make-posn 30 20) 5 5 'blue)
              (cons (make-trangle (make-posn 65 20) 5 5 'blue)
                    (cons (make-trangle (make-posn 40 75) 20 10 'red)
                          (cons (make-trangle (make-posn 45 35) 10 30 'blue) empty))))))
(define (fun-for-losh shap-list)
  (cond
    [(empty? shap-list) true]
    [else (and (cond
            [(circle? (first shap-list)) ...]
            [(trangle? (first shap-list)) ...]
            ) (fun-for-losh (rest shap-list)))]
    ))
;;读取列的元素并绘制表
(define (draw-losh shap-list)
  (cond
    [(empty? shap-list) true]
    [else (and (cond
            [(circle? (first shap-list)) (draw-circle (circle-posn (first shap-list)) (circle-banjin (first shap-list)) (circle-color (first shap-list)))]
            [(trangle? (first shap-list)) (draw-solid-rect (trangle-posn (first shap-list)) (trangle-lang (first shap-list)) (trangle-width (first shap-list)) (trangle-color (first shap-list)))]
            ) (draw-losh (rest shap-list)))]
    ))

;;移动表并返回移动后的列表
(define (translate-losh shap-list delta)
  (cond
    [(empty? shap-list) empty]
    [else (cond
            [(circle? (first shap-list))
             (cons
              (make-circle (make-posn (+ (posn-x (circle-posn (first shap-list))) delta) (posn-y (circle-posn (first shap-list)))) (circle-banjin (first shap-list)) (circle-color (first shap-list)))
              (translate-losh (rest shap-list) delta))]
            [(trangle? (first shap-list))
             (cons
              (make-trangle (make-posn (+ (posn-x (trangle-posn (first shap-list))) delta) (posn-y (trangle-posn (first shap-list)))) (trangle-lang (first shap-list)) (trangle-width (first shap-list)) (trangle-color (first shap-list)))
              (translate-losh (rest shap-list) delta))]
            )
             ]
    ))
;清除列表元素
(define (clear-losh shap-list)
  (cond
    [(empty? shap-list) true]
    [else (and (cond
            [(circle? (first shap-list))
             (clear-circle (circle-posn (first shap-list)) (circle-banjin (first shap-list)) (circle-color (first shap-list)))]
            [(trangle? (first shap-list)) (clear-solid-rect (trangle-posn (first shap-list)) (trangle-lang (first shap-list)) (trangle-width (first shap-list)) (trangle-color (first shap-list)))]
            ) (clear-losh (rest shap-list)))]
    ))
;;绘制 清除 移动 再绘制串联起来
(define (draw-and-clear shap-list)
  (and (and (draw-losh shap-list) (sleep-for-a-while 0.1)) (clear-losh shap-list)))

(define (move-picture delta shap-list)
  (cond
    [(draw-and-clear shap-list) (translate-losh shap-list delta)]
    [else shap-list]))

(define (apply-n face n)
  (cond
    [(zero? n) (draw-losh face)]
    [else  (apply-n (move-picture 10 face) (sub1 n))]))

;;start
(start 300 100)
(apply-n face 18)
;(draw-losh
;(move-picture
;(move-picture
; (move-picture 10 face)23)-5)
;)


;;(start 500 100)
;;(control-left-right face 100 move-picture draw-losh)