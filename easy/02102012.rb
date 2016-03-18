#!/usr/bin/ruby

puts "Mass? "
mass = gets.chomp.to_f

puts "Acceleration? "
acceleration = gets.chomp.to_f

puts "Force = " + (mass * acceleration).to_s
