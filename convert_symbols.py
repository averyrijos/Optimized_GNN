#!/usr/bin/env python3
"""Convert mathematical symbols to LaTeX in substrate_theory.md"""

def convert_symbols(text):
    """Convert mathematical symbols to LaTeX format"""
    # Lambda symbols - fix mixed cases first
    text = text.replace('$\\Lambda$ᵢ', '$\\Lambda_i$')
    text = text.replace('$\\Lambda$ᵢ₊₁', '$\\Lambda_{i+1}$')
    text = text.replace('$\\Lambda$ᵢ₋₁', '$\\Lambda_{i-1}$')
    
    # Lambda symbols
    text = text.replace('Λ', '$\\Lambda$')
    text = text.replace('Λᵢ', '$\\Lambda_i$')
    text = text.replace('Λᵢ₊₁', '$\\Lambda_{i+1}$')
    text = text.replace('Λᵢ₋₁', '$\\Lambda_{i-1}$')
    
    # Greek letters - fix mixed cases first
    text = text.replace('$\\Phi$ᵢ', '$\\Phi_i$')
    text = text.replace('$\\pi$ᵢ', '$\\pi_i$')
    
    # Greek letters
    text = text.replace('Φ', '$\\Phi$')
    text = text.replace('Φᵢ', '$\\Phi_i$')
    text = text.replace('Φ($\\Lambda$)', '$\\Phi(\\Lambda)$')
    text = text.replace('πᵢ', '$\\pi_i$')
    text = text.replace('φ', '$\\phi$')
    text = text.replace('δ_min', '$\\delta_{min}$')
    text = text.replace('δ₋', '$\\delta_-$')
    text = text.replace('δ', '$\\delta$')
    
    # Variables with subscripts - fix mixed cases first
    text = text.replace('$D_i$ᵢ', '$D_i$')
    text = text.replace('$S_i$ᵢ', '$S_i$')
    
    # Variables with subscripts
    text = text.replace('Dᵢ', '$D_i$')
    text = text.replace('Sᵢ', '$S_i$')
    text = text.replace('I($\\Lambda$ᵢ)', '$I(\\Lambda_i)$')
    text = text.replace('I(Λᵢ)', '$I(\\Lambda_i)$')
    text = text.replace('I(Λ)', '$I(\\Lambda)$')
    text = text.replace('|I($\\Lambda$ᵢ)|', '$|I(\\Lambda_i)|$')
    text = text.replace('|I(Λᵢ)|', '$|I(\\Lambda_i)|$')
    text = text.replace('|Sᵢ|', '$|S_i|$')
    text = text.replace('|$S_i$ᵢ|', '$|S_i|$')
    
    # Mathematical symbols
    text = text.replace('∃', '$\\exists$')
    text = text.replace('∀', '$\\forall$')
    text = text.replace('∈', '$\\in$')
    text = text.replace('∅', '$\\emptyset$')
    text = text.replace('→', '$\\to$')
    text = text.replace('≥', '$\\geq$')
    text = text.replace('≤', '$\\leq$')
    text = text.replace('∘', '$\\circ$')
    
    # Special cases that might not have been caught
    text = text.replace("P'", "$P'$")
    text = text.replace('r_reg', '$r_{reg}$')
    text = text.replace('r_inj', '$r_{inj}$')
    text = text.replace('r_deg', '$r_{deg}$')
    text = text.replace('Δ$D_i$ᵢ', '$\\Delta D_i$')
    text = text.replace('ΔDᵢ', '$\\Delta D_i$')
    text = text.replace('Δt', '$\\Delta t$')
    text = text.replace('D₀', '$D_0$')
    text = text.replace('T_collapse', '$T_{collapse}$')
    
    return text
    
    return text

# Read the file
with open('/workspaces/Optimized_GNN/substrate_theory.md', 'r') as f:
    content = f.read()

# Convert symbols
converted_content = convert_symbols(content)

# Write back to file
with open('/workspaces/Optimized_GNN/substrate_theory.md', 'w') as f:
    f.write(converted_content)

print("Symbol conversion completed!")
