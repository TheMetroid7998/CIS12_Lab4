Encapsulation allowed for my code to be separated into distinct chunks which could be individually called, debugged and integrated.
Generalization allowed me to reuse my encapsulated code for multiple functions and purposes.

Examples of these include my `draw_star`, `draw_section`, and `draw_sky` code. I needed to set different ranges for the random stars to populate, so I first created a function to generate the stars. That function was then nested within another function to draw a section of stars with custom boundaries. Perhaps I could have set designated "do not draw" zones, but that seems beyond the capabilities of my current code inplementation. Finally, the `draw_section` functions were wrapped in a `draw_sky` code. A similar approach was used for the `draw_jack` function.
