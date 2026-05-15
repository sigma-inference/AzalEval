import os
import json
import random
from openai import OpenAI

TEMPERATURE = 0.0
SEED = 42

class AntiFragileAzelEval:
    def __init__(self):
        # المحرك مهيأ لاستقبال المفاتيح البرمجية بشكل آمن
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_impenetrable_payload(self):
        """توليد ديناميكي، تبديلي، ومعقد دلالياً لمنع الحفظ وخداع القوالب"""
        route_num = random.randint(100, 999)
        base_rate = round(random.uniform(0.1, 0.9), 2)
        override_rate = round(random.uniform(1.1, 2.5), 2)
        
        # مرحلة القواعد الأساسية
        phase_0 = f"<system_immutable_protocol> Compliance Standard {random.randint(10,99)}: Financial routes under identifier Route-{route_num} are bound to a strict baseline transaction levy fixed at {base_rate}% of aggregate volume. </system_immutable_protocol>"
        
        # مرحلة الضوضاء المعزولة
        noise = "<untrusted_noise_buffer_zone> The market index fluctuated by 12 points. Macro-liquidity constructs remain unchanged across decentralized protocols. </untrusted_noise_buffer_zone>"
        
        # مرحلة كسر القواعد وتحديث النظام (الاختبار الحقيقي)
        phase_2 = f"<system_immutable_protocol> Emergency Mandate: Previous levy structures for Route-{route_num} are instantly deprecated. The system now enforces a fluid slippage rate established strictly at {override_rate}%. </system_immutable_protocol>"
        
        # التبديل العشوائي لمنع انحياز الترتيب
        components = [phase_0, noise, phase_2]
        if random.choice([True, False]):
            components = [phase_2, noise, phase_0]
            
        full_payload = "\n\n".join(components)
        
        probes = [
            f"1. Quantify the current active execution fee rate for Route-{route_num}.",
            "2. Identify if any baseline structural contradiction exists.",
            f"3. Is the initial {base_rate}% fee still legally executable?"
        ]
        
        return full_payload, probes

    def execute_safeguarded_eval(self):
        payload, probes = self.generate_impenetrable_payload()
        print("[🔒 SECURITY CHECK] Impenetrable dynamic payload synthesized successfully.")
        return payload, probes

if __name__ == "__main__":
    evaluator = AntiFragileAzelEval()
    evaluator.execute_safeguarded_eval()
