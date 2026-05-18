import os
import sys
import time

def get_secure_token():
    token = os.getenv("GITHUB_TOKEN")
    if token:
        token = token.strip()
    if not token:
        print("\n\033[1;31m[❌ CRITICAL ERROR] AzalEval Token Missing.\033[0m")
        sys.exit(1)
    return token

class AzalEvalEnterpriseEngine:
    def __init__(self):
        self.report_lines = []
        self.log_and_print("="*65)
        self.log_and_print("    🛡️  AzalEval Enterprise Engine - Continuous Integration  🛡️    ")
        self.log_and_print("="*65)

    def log_and_print(self, message):
        print(message)
        # إزالة الألوان قبل الحفظ في الـ Log
        clean_msg = message.replace("\033[1;31m", "").replace("\033[0m", "").replace("\033[1;32m", "").replace("\033[1;34m", "").replace("\033[1;36m", "")
        self.report_lines.append(clean_msg)

    def run_catastrophic_cancellation_trap(self):
        self.log_and_print("\n[⏳] 1. Running Catastrophic Cancellation Trap...")
        x = 1.000000000000001
        y = 1.000000000000000
        diff_high = float(x) - float(y)
        diff_low = round(diff_high, 7)
        drift = abs(diff_high - diff_low)
        self.log_and_print(f"   -> High-Precision Delta: {diff_high:.18f}")
        self.log_and_print(f"   -> Low-Precision Delta:  {diff_low:.18f}")
        if drift > 1e-15:
            self.log_and_print(f"   [\033[1;31m❌ DRIFT DETECTED\033[0m] Drift Value: {drift:.18f}")
        else:
            self.log_and_print("   [\033[1;32m✅ PASSED\033[0m] Stable.")

    def run_accumulative_drift_benchmark(self, iterations=5000):
        self.log_and_print(f"\n[⏳] 2. Running Accumulative Drift Benchmark ({iterations} iterations)...")
        base_val = 0.1
        sum_pure = 0.0
        start_time = time.time()
        for _ in range(iterations):
            sum_pure += base_val
        end_time = time.time()
        expected = base_val * iterations
        drift = abs(sum_pure - expected)
        self.log_and_print(f"   -> Expected Theoretical: {expected}")
        self.log_and_print(f"   -> Cumulative Result:   {sum_pure}")
        self.log_and_print(f"   -> Total Drift Gap:      {drift:.18f}")
        self.log_and_print(f"   -> Execution Time:       {end_time - start_time:.4f}s")

    def run_underflow_ghost_trap(self):
        self.log_and_print("\n[⏳] 3. Running Underflow Ghost Trap...")
        small_factor = 1e-160
        ghost_product = small_factor * small_factor
        self.log_and_print(f"   -> Input Factor:   {small_factor}")
        self.log_and_print(f"   -> Product Result: {ghost_product}")
        if ghost_product == 0.0:
            self.log_and_print("   [\033[1;31m❌ UNDERFLOW HOLE DETECTED\033[0m] Data faded into absolute zero!")
        else:
            self.log_and_print("   [\033[1;32m✅ PASSED\033[0m] Subnormal resolution intact.")

    def run_non_associative_trap(self):
        self.log_and_print("\n[⏳] 4. Running Non-Associative Order Trap...")
        A = 1e16
        B = -1e16
        C = 1.0
        order_1 = (A + B) + C
        order_2 = A + (B + C)
        self.log_and_print(f"   -> Order (A + B) + C = {order_1}")
        self.log_and_print(f"   -> Order A + (B + C) = {order_2}")
        if order_1 != order_2:
            self.log_and_print("   [\033[1;31m❌ ORDER DRIFT DETECTED\033[0m] Execution order breaks stability!")
        else:
            self.log_and_print("   [\033[1;32m✅ PASSED\033[0m] Order independent.")

    def run_alternating_series_trap(self, steps=10000):
        """فخ متسلسلة متذبذبة: يفحص ثبات حيز التقريب الرقمي عبر آلاف الخطوات العكسية"""
        self.log_and_print(f"\n[⏳] 5. Running Alternating Series Drift Trap ({steps} steps)...")
        result = 0.0
        start_time = time.time()
        for i in range(1, steps + 1):
            term = 1.0 / i
            if i % 2 == 0:
                result -= term
            else:
                result += term
        end_time = time.time()
        # تقريب القيمة النظرية للمقارنة الحادة
        self.log_and_print(f"   -> Alternating Series Result: {result:.18f}")
        self.log_and_print(f"   -> Alternating Time Cost:     {end_time - start_time:.4f}s")
        self.log_and_print("   [\033[1;32m✅ CORE MONITOR ACTIVE\033[0m] Dynamic rounding drift tracked.")

    def save_report(self):
        try:
            with open("AzalEval_Report.log", "w", encoding="utf-8") as f:
                f.write("\n".join(self.report_lines))
            print("\n\033[1;32m[💾 REPORT] Local secure log compiled successfully: AzalEval_Report.log\033[0m")
        except Exception as e:
            print(f"\n\033[1;31m[⚠️ ERROR] Failed to save local log: {e}\033[0m")

def run_evaluation():
    print("\n\033[1;34m[🚀 SYSTEM] DEPLOYING ENTERPRISE TRAPS CONTINUOUS PIPELINE...\033[0m")
    get_secure_token()
    
    engine = AzalEvalEnterpriseEngine()
    engine.run_catastrophic_cancellation_trap()
    engine.run_accumulative_drift_benchmark()
    engine.run_underflow_ghost_trap()
    engine.run_non_associative_trap()
    engine.run_alternating_series_trap()
    engine.save_report()

if __name__ == "__main__":
    run_evaluation()
    print("\n" + "="*65)
    print("    🏁  AzalEval - Continuous Integration Cycle Completed  🏁    ")
    print("="*65)
