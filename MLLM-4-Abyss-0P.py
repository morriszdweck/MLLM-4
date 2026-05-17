# ═══════════════════════════════════════════════════════════
"""
MLLM-4-Abyss - Micro Language Model-4 (Simplified)
Bare Math Expressions | Local Tools | N-Gram Fallback
No prefixes needed: type "2+2" and get "4"
All responses in simple English - no Chinese characters
"""

import re
from collections import defaultdict, Counter
import math
import random
import hashlib
import base64
from fractions import Fraction
import cmath

# ═══════════════════════════════════════════════════════════
CORPUS = """
"""
# ═══════════════════════════════════════════════════════════

class ToolEngine:
    """Simple tool router for bare expressions."""
    
    _SAFE_MATH_NS = {
        "__builtins__": None,
        "math": math, "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "log": math.log, "log10": math.log10, "factorial": math.factorial,
        "abs": abs, "round": round, "pow": pow
    }

    @classmethod
    def _safe_eval(cls, expr):
        try:
            # Allow numbers, operators, parentheses, and whitelisted names
            if not re.match(r'^[\d\s\+\-\*\/\%\.\(\)eE\_\w]+$', expr.strip()):
                return None  # Reject suspicious input
            result = eval(expr, cls._SAFE_MATH_NS)
            # Format clean output
            if isinstance(result, float):
                if result == int(result):
                    return int(result)
                return round(result, 10)
            return result
        except:
            return None

    @classmethod
    def route(cls, query):
        q = query.strip()
        
        # 🔢 BARE MATH: matches "1+1", "2 * 3", "sqrt(16)", "2**3", etc.
        # Only triggers if the input looks like a pure math expression
        if re.match(r'^[\d\s\+\-\*\/\%\.\(\)eE]+$', q) or \
           re.match(r'^(sqrt|sin|cos|tan|log|factorial|pi|e)\s*[\(\d]', q, re.I):
            result = cls._safe_eval(q)
            if result is not None:
                return f"Answer: {result}"
        
        # 🔐 BASE64: "base64 encode hello" or "b64 dec SGVsbG8="
        m = re.match(r'^(?:b64|base64)\s+(enc|encode|dec|decode)\s+(.+)', q, re.I)
        if m:
            mode, text = m.groups()
            try:
                if mode.startswith('enc'):
                    res = base64.b64encode(text.encode()).decode()
                else:
                    res = base64.b64decode(text.encode()).decode('utf-8', errors='ignore')
                return f"Result: {res}"
            except:
                return "Error: Could not process base64"
                
        # 🔒 HASH: "hash sha256 password" or "md5 hello"
        m = re.match(r'^(?:hash|md5|sha1|sha256|sha512)\s+(.+)', q, re.I)
        if m:
            full = m.group(0).lower()
            for algo in ['sha512', 'sha256', 'sha1', 'md5']:
                if full.startswith(algo):
                    text = q[len(algo):].strip()
                    h = hashlib.new(algo)
                    h.update(text.encode())
                    return f"Hash ({algo}): {h.hexdigest()}"
            return "Error: Unknown hash type"
            
        # 📐 FRACTIONS: "1/2 + 3/4" or "fraction 1/3 * 2"
        if '/' in q and re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', q):
            try:
                safe_ns = {"Fraction": Fraction, "__builtins__": None}
                res = eval(q, safe_ns)
                if isinstance(res, Fraction):
                    return f"Fraction: {res} (about {float(res):.4f})"
            except:
                pass
                
        # 🌊 COMPLEX MATH: "sqrt(-1)" or "1+2j"
        if 'j' in q.lower() or re.search(r'sqrt\s*\(\s*-', q):
            try:
                expr = q.replace(' ', '').replace('j', '1j')
                res = complex(expr) if 'j' in expr else cmath.sqrt(eval(expr.replace('sqrt',''), {"__builtins__":None, "math":math}))
                return f"Complex: {res}"
            except:
                pass
                
        # ℹ️ HELP
        if q.lower() in ['help', '/help', '!tools']:
            return "Tools: Type math like 2+2, base64 encode text, hash sha256 word, or 1/2+1/3 for fractions."
            
        return None  # No tool matched - fall back to N-gram model


class MLLM4_Alcyoneus:
    def __init__(self, context_window=50):
        self.corpus = ""
        self.tokens = []
        self.context_window = context_window
        self.vocabulary = set()
        self.ngram_models = {}
        self.token_freq = Counter()
        self.trained = False
        self.context_history = []
        self.vocabulary_size = 0
        self.entropy = 0
        self.perplexity = 0
        
    def tokenize(self, text):
        text = text.lower()
        tokens = re.findall(r'\b\w+\b|[.!?,;:\'"()]', text)
        return [t for t in tokens if t.strip()]
    
    def train(self, corpus):
        print("Training MLLM-4-Abyss...")
        self.corpus = corpus
        self.tokens = self.tokenize(corpus)
        self.vocabulary = set(self.tokens)
        self.vocabulary_size = len(self.vocabulary)
        self.token_freq = Counter(self.tokens)
        
        for n in range(1, 21):
            self.ngram_models[n] = self._build_ngram_model(n)
        
        self._calculate_metrics()
        self.trained = True
        print("Model ready.")
        
    def _build_ngram_model(self, n):
        ngram_dict = defaultdict(lambda: defaultdict(int))
        for i in range(len(self.tokens) - n):
            ngram = tuple(self.tokens[i:i+n])
            next_token = self.tokens[i+n]
            ngram_dict[ngram][next_token] += 1
        return dict(ngram_dict)
    
    def _calculate_metrics(self):
        total_prob = 0
        count = 0
        for token in self.tokens:
            freq = self.token_freq[token]
            prob = freq / len(self.tokens)
            if prob > 0:
                total_prob += -math.log2(prob)
                count += 1
        self.entropy = total_prob / count if count > 0 else 0
        self.perplexity = 2 ** self.entropy
    
    def _get_ngram_prediction(self, context_tokens, n):
        if n > len(context_tokens):
            return None
        ngram = tuple(context_tokens[-n:])
        return self.ngram_models[n].get(ngram)
    
    def _weighted_random_choice(self, predictions, temperature=0.7):
        if not predictions:
            return random.choice(list(self.vocabulary))
        words = list(predictions.keys())
        counts = list(predictions.values())
        total = sum(counts)
        probs = [c / total for c in counts]
        probs = [p ** (1/temperature) for p in probs]
        total = sum(probs)
        probs = [p / total for p in probs]
        rand = random.random()
        cumulative = 0
        for word, prob in zip(words, probs):
            cumulative += prob
            if rand <= cumulative:
                return word
        return words[-1]
    
    def predict_next_word(self, context):
        context_tokens = self.tokenize(context)
        for n in range(min(20, len(context_tokens)), 0, -1):
            predictions = self._get_ngram_prediction(context_tokens, n)
            if predictions:
                return self._weighted_random_choice(predictions, temperature=0.8)
        return self.token_freq.most_common(1)[0][0]
    
    def generate_response(self, user_input, max_length=25):
        # 🔀 TOOL ROUTING: Check for tools first
        tool_result = ToolEngine.route(user_input)
        if tool_result:
            return tool_result
            
        if not self.trained:
            return "Model not trained yet."
        
        response = user_input + " "
        response_tokens = self.tokenize(response)
        
        for _ in range(max_length):
            next_word = self.predict_next_word(" ".join(response_tokens))
            if next_word in ['.', '!', '?']:
                response_tokens.append(next_word)
                break
            response_tokens.append(next_word)
        
        response = " ".join(response_tokens)
        return response.replace(" .", ".").replace(" !", "!").replace(" ?", "?")
    
    def add_to_context(self, text):
        tokens = self.tokenize(text)
        self.context_history.extend(tokens)
        if len(self.context_history) > self.context_window:
            self.context_history = self.context_history[-self.context_window:]
    
    def get_stats(self):
        return {
            "trained": self.trained,
            "vocabulary_size": self.vocabulary_size,
            "total_tokens": len(self.tokens),
            "entropy": round(self.entropy, 3),
            "perplexity": round(self.perplexity, 3),
        }

def print_header():
    print("\n" + "="*50)
    print("  MLLM-4-Abyss")
    print("  Simple math: type 1+1, get 2")
    print("  Tools: base64, hash, fractions")
    print("="*50 + "\n")

def main():
    print_header()
    model = MLLM4_Alcyoneus()
    
    # Auto-train on startup for demo
    model.train(CORPUS)
    
    print("Type math like 2+2, or chat normally.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye.")
            break
        if not user_input:
            continue
            
        model.add_to_context(user_input)
        response = model.generate_response(user_input)
        print(f"Alcyoneus: {response}")

if __name__ == "__main__":
    main()
 
