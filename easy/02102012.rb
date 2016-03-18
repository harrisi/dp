#!/usr/bin/ruby

puts "Mass? "
mass = gets.chomp.to_i

puts "Acceleration? "
acceleration = gets.chomp.to_i

puts "Force = " + (mass * acceleration).to_s
