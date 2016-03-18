#!/usr/local/bin/racket
#lang racket

(define (start)
  ;; These will constantly be shrinking the search space for random. A better
  ;; implementation would be a binary search, although this behaves similarly
  ;; to a binary search, although it is implemented much more naively.
  (define current-low 1) ;; State for the current lowest guess
  (define current-high 101) ;; current highest guess
  (let/ec break
    (let loop ()
      ;; guess on each loop based on current search space
      (define my-guess (random current-low current-high))
      ;; loop for unknown inputs so that unknown inputs don't cause a new random
      ;; number
      (let unknown ()
        (display (format "Is your number ~a? (y)es, (h)igher, (l)ower~n"
                         my-guess))
        (define input (read))
        (cond
          ([eq? input 'y]
           (displayln "I win!")
           (break))
          ([eq? input 'h]
           ;; if the number to be guessed is higher than the current number, the
           ;; current number + 1 is now the current lowest possible guess.
           (set! current-low (add1 my-guess)))
          ([eq? input 'l]
           ;; if the number to be guessed is lower than the current number, the
           ;; current number is now the current highest possible guess.
           (set! current-high my-guess))
          (else
           ;; if input is not y, h, or l, just loop again.
           (displayln (format "unknown input ~a" input))
           (unknown))))
      (loop))))

(module+ main
  (start))
