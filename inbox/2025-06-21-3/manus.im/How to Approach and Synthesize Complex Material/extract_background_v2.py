#!/usr/bin/env python3
import re
import json
import os

def extract_background_conversation_v2(file_path):
    """
    Enhanced extraction for background conversation with better format handling
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Look for text content patterns
        text_patterns = [
            r'"text":\s*"([^"]*(?:\\.[^"]*)*)"',  # JSON text fields
            r'"text":\s*"([^"]+)"',  # Simple text fields
        ]
        
        conversation_turns = []
        turn_number = 0
        
        # Find role and text pairs
        role_pattern = r'"role":\s*"(user|model)"'
        roles = re.findall(role_pattern, content)
        
        # Extract text content more robustly
        text_matches = []
        for pattern in text_patterns:
            matches = re.findall(pattern, content, re.DOTALL)
            text_matches.extend(matches)
        
        # Try to pair roles with text content
        for i, role in enumerate(roles):
            if i < len(text_matches):
                turn_number += 1
                text_content = text_matches[i]
                
                # Clean up escaped characters
                text_content = text_content.replace('\\"', '"')
                text_content = text_content.replace('\\n', '\n')
                text_content = text_content.replace('\\t', '\t')
                
                # Skip very short or empty content
                if len(text_content.strip()) < 10:
                    continue
                
                turn_data = {
                    'turn': turn_number,
                    'role': role,
                    'text': text_content,
                    'length': len(text_content),
                    'confusion_markers': [],
                    'attribution_notes': [],
                    'key_concepts': []
                }
                
                # Analyze content for key concepts and confusion markers
                analyze_turn_content(turn_data)
                
                conversation_turns.append(turn_data)
        
        return conversation_turns
        
    except Exception as e:
        print(f"Error in v2 extraction: {e}")
        return None

def analyze_turn_content(turn_data):
    """
    Analyze individual turn for concepts, confusion markers, and attribution notes
    """
    text = turn_data['text'].lower()
    
    # Confusion markers
    confusion_indicators = [
        'i apologize for the confusion',
        'let me clarify',
        'i made an error',
        'correction:',
        'actually,',
        'wait, let me reconsider',
        'i misspoke',
        'to be clear',
        'let me rephrase'
    ]
    
    for indicator in confusion_indicators:
        if indicator in text:
            turn_data['confusion_markers'].append(indicator)
    
    # Key concept detection
    key_concepts = [
        'consciousness',
        'hofstadter',
        'system 1',
        'system 2', 
        'system 3',
        'holographic',
        'strange loop',
        'convolution',
        'memetic',
        'grok',
        'decoherence',
        'alignment',
        'cognitive',
        'linguistic',
        'workspace',
        'irreducible',
        'private',
        'field',
        'substrate',
        'emergence',
        'recursion',
        'self-reference',
        'meaning',
        'смысл'
    ]
    
    for concept in key_concepts:
        if concept in text:
            turn_data['key_concepts'].append(concept)
    
    # Attribution notes based on content patterns
    if 'i am' in text or 'my identity' in text:
        turn_data['attribution_notes'].append('identity_discussion')
    
    if len(turn_data['text']) > 2000:
        turn_data['attribution_notes'].append('long_detailed_response')
    
    if 'framework' in text and 'theory' in text:
        turn_data['attribution_notes'].append('theoretical_framework_discussion')

def create_background_analysis(conversation_turns):
    """
    Create comprehensive analysis of the background conversation
    """
    if not conversation_turns:
        return None
    
    analysis = {
        'metadata': {
            'total_turns': len(conversation_turns),
            'user_turns': len([t for t in conversation_turns if t['role'] == 'user']),
            'model_turns': len([t for t in conversation_turns if t['role'] == 'model']),
            'total_length': sum(t['length'] for t in conversation_turns),
            'avg_turn_length': sum(t['length'] for t in conversation_turns) / len(conversation_turns)
        },
        'content_analysis': {
            'confusion_turns': len([t for t in conversation_turns if t['confusion_markers']]),
            'theoretical_turns': len([t for t in conversation_turns if 'theoretical_framework_discussion' in t['attribution_notes']]),
            'identity_discussions': len([t for t in conversation_turns if 'identity_discussion' in t['attribution_notes']]),
            'key_concept_frequency': {}
        },
        'conversation_phases': [],
        'key_insights': [],
        'attribution_timeline': []
    }
    
    # Analyze key concept frequency
    all_concepts = []
    for turn in conversation_turns:
        all_concepts.extend(turn['key_concepts'])
    
    for concept in set(all_concepts):
        analysis['content_analysis']['key_concept_frequency'][concept] = all_concepts.count(concept)
    
    # Identify conversation phases based on topic shifts
    current_phase = {
        'phase_number': 1,
        'start_turn': 1,
        'dominant_concepts': [],
        'description': 'Initial phase'
    }
    
    phase_concepts = []
    for i, turn in enumerate(conversation_turns):
        phase_concepts.extend(turn['key_concepts'])
        
        # Detect phase shifts (simplified heuristic)
        if (i > 0 and i % 10 == 0) or i == len(conversation_turns) - 1:
            current_phase['end_turn'] = turn['turn']
            current_phase['dominant_concepts'] = list(set(phase_concepts))
            analysis['conversation_phases'].append(current_phase.copy())
            
            # Start new phase
            current_phase = {
                'phase_number': current_phase['phase_number'] + 1,
                'start_turn': turn['turn'] + 1,
                'dominant_concepts': [],
                'description': f'Phase {current_phase["phase_number"] + 1}'
            }
            phase_concepts = []
    
    return analysis

def save_background_analysis(conversation_turns, analysis, output_dir):
    """
    Save comprehensive background analysis
    """
    # Save conversation data
    with open(os.path.join(output_dir, 'background_conversation_v2.json'), 'w', encoding='utf-8') as f:
        json.dump(conversation_turns, f, indent=2, ensure_ascii=False)
    
    # Save analysis
    with open(os.path.join(output_dir, 'background_analysis_v2.json'), 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    
    # Save readable summary
    with open(os.path.join(output_dir, 'background_summary.md'), 'w', encoding='utf-8') as f:
        f.write("# Background Conversation Analysis\n\n")
        f.write("## Metadata\n")
        f.write(f"- Total turns: {analysis['metadata']['total_turns']}\n")
        f.write(f"- User turns: {analysis['metadata']['user_turns']}\n")
        f.write(f"- Model turns: {analysis['metadata']['model_turns']}\n")
        f.write(f"- Total length: {analysis['metadata']['total_length']:,} characters\n")
        f.write(f"- Average turn length: {analysis['metadata']['avg_turn_length']:.0f} characters\n\n")
        
        f.write("## Content Analysis\n")
        f.write(f"- Confusion turns: {analysis['content_analysis']['confusion_turns']}\n")
        f.write(f"- Theoretical framework discussions: {analysis['content_analysis']['theoretical_turns']}\n")
        f.write(f"- Identity discussions: {analysis['content_analysis']['identity_discussions']}\n\n")
        
        f.write("## Key Concepts (Frequency)\n")
        sorted_concepts = sorted(analysis['content_analysis']['key_concept_frequency'].items(), 
                               key=lambda x: x[1], reverse=True)
        for concept, freq in sorted_concepts[:20]:  # Top 20
            f.write(f"- {concept}: {freq}\n")
        
        f.write(f"\n## Conversation Phases\n")
        for phase in analysis['conversation_phases']:
            f.write(f"### Phase {phase['phase_number']} (Turns {phase['start_turn']}-{phase['end_turn']})\n")
            f.write(f"Dominant concepts: {', '.join(phase['dominant_concepts'][:10])}\n\n")
    
    print(f"Background analysis complete!")
    print(f"Extracted {len(conversation_turns)} conversation turns")
    print(f"Total content: {analysis['metadata']['total_length']:,} characters")
    print(f"Key concepts identified: {len(analysis['content_analysis']['key_concept_frequency'])}")

if __name__ == "__main__":
    input_file = "/home/ubuntu/upload/background.sh"
    output_dir = "/home/ubuntu/theory_analysis/background_analysis"
    
    print("Extracting background conversation (v2)...")
    conversation_turns = extract_background_conversation_v2(input_file)
    
    if conversation_turns:
        print("Creating comprehensive analysis...")
        analysis = create_background_analysis(conversation_turns)
        
        print("Saving results...")
        save_background_analysis(conversation_turns, analysis, output_dir)
    else:
        print("Failed to extract conversation")

