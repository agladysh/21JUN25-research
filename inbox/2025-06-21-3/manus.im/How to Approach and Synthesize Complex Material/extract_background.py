#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime

def extract_background_conversation(file_path):
    """
    Extract conversation from background.sh file with enhanced attribution tracking
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find the JSON content within the curl command
        json_match = re.search(r'"contents":\s*(\[.*?\])', content, re.DOTALL)
        if not json_match:
            print("No JSON content found in the expected format")
            return None
        
        json_str = json_match.group(1)
        
        # Parse the JSON
        try:
            contents = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return None
        
        # Extract conversation turns with enhanced attribution
        conversation = []
        turn_number = 0
        
        for item in contents:
            if 'parts' in item and 'role' in item:
                turn_number += 1
                role = item['role']
                
                # Extract text content
                text_parts = []
                for part in item['parts']:
                    if 'text' in part:
                        text_parts.append(part['text'])
                
                if text_parts:
                    turn_data = {
                        'turn': turn_number,
                        'role': role,
                        'text': '\n'.join(text_parts),
                        'timestamp': None,  # Will be filled if available
                        'confusion_markers': [],
                        'attribution_notes': []
                    }
                    
                    # Check for potential LLM confusion markers
                    text_content = turn_data['text'].lower()
                    confusion_indicators = [
                        'i apologize for the confusion',
                        'let me clarify',
                        'i made an error',
                        'correction:',
                        'actually,',
                        'wait, let me reconsider'
                    ]
                    
                    for indicator in confusion_indicators:
                        if indicator in text_content:
                            turn_data['confusion_markers'].append(indicator)
                    
                    # Mark potential beginning/end confusion
                    if turn_number <= 3:
                        turn_data['attribution_notes'].append('potential_beginning_confusion')
                    
                    conversation.append(turn_data)
        
        return conversation
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

def analyze_conversation_structure(conversation):
    """
    Analyze the structure and patterns in the conversation
    """
    if not conversation:
        return None
    
    analysis = {
        'total_turns': len(conversation),
        'user_turns': len([t for t in conversation if t['role'] == 'user']),
        'model_turns': len([t for t in conversation if t['role'] == 'model']),
        'confusion_turns': len([t for t in conversation if t['confusion_markers']]),
        'potential_confusion_areas': [],
        'conversation_phases': [],
        'key_topics': []
    }
    
    # Identify potential confusion areas
    for turn in conversation:
        if turn['confusion_markers'] or 'potential_beginning_confusion' in turn['attribution_notes']:
            analysis['potential_confusion_areas'].append({
                'turn': turn['turn'],
                'role': turn['role'],
                'markers': turn['confusion_markers'],
                'notes': turn['attribution_notes']
            })
    
    # Identify conversation phases (rough topic changes)
    current_phase = {'start': 1, 'topic_indicators': []}
    phase_number = 1
    
    for i, turn in enumerate(conversation):
        # Simple heuristic for topic changes (long user messages often indicate new topics)
        if turn['role'] == 'user' and len(turn['text']) > 500:
            if i > 0:  # End current phase
                current_phase['end'] = i
                current_phase['phase'] = phase_number
                analysis['conversation_phases'].append(current_phase.copy())
                phase_number += 1
                current_phase = {'start': i + 1, 'topic_indicators': []}
    
    # Add final phase
    if current_phase['start'] <= len(conversation):
        current_phase['end'] = len(conversation)
        current_phase['phase'] = phase_number
        analysis['conversation_phases'].append(current_phase)
    
    return analysis

def save_analysis_results(conversation, analysis, output_dir):
    """
    Save the extracted conversation and analysis results
    """
    import os
    
    # Save raw conversation
    with open(os.path.join(output_dir, 'background_conversation.json'), 'w', encoding='utf-8') as f:
        json.dump(conversation, f, indent=2, ensure_ascii=False)
    
    # Save analysis
    with open(os.path.join(output_dir, 'conversation_analysis.json'), 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    
    # Save readable text version
    with open(os.path.join(output_dir, 'background_conversation.txt'), 'w', encoding='utf-8') as f:
        f.write("# Background Conversation Analysis\n\n")
        f.write(f"Total turns: {analysis['total_turns']}\n")
        f.write(f"User turns: {analysis['user_turns']}\n")
        f.write(f"Model turns: {analysis['model_turns']}\n")
        f.write(f"Potential confusion turns: {analysis['confusion_turns']}\n\n")
        
        f.write("## Conversation Content\n\n")
        for turn in conversation:
            f.write(f"### Turn {turn['turn']} ({turn['role']})\n")
            if turn['confusion_markers']:
                f.write(f"**CONFUSION MARKERS**: {', '.join(turn['confusion_markers'])}\n")
            if turn['attribution_notes']:
                f.write(f"**ATTRIBUTION NOTES**: {', '.join(turn['attribution_notes'])}\n")
            f.write(f"{turn['text']}\n\n")
            f.write("---\n\n")
    
    print(f"Analysis complete. Results saved to {output_dir}")
    print(f"Total conversation turns: {analysis['total_turns']}")
    print(f"Potential confusion areas: {analysis['confusion_turns']}")
    print(f"Conversation phases identified: {len(analysis['conversation_phases'])}")

if __name__ == "__main__":
    input_file = "/home/ubuntu/upload/background.sh"
    output_dir = "/home/ubuntu/theory_analysis/background_analysis"
    
    print("Extracting background conversation...")
    conversation = extract_background_conversation(input_file)
    
    if conversation:
        print("Analyzing conversation structure...")
        analysis = analyze_conversation_structure(conversation)
        
        print("Saving results...")
        save_analysis_results(conversation, analysis, output_dir)
    else:
        print("Failed to extract conversation")
        sys.exit(1)

