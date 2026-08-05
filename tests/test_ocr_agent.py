from agents.ocr_correction_agent import OCRCorrectionAgent

agent = OCRCorrectionAgent()

sample = """
Employec Leavc Poliey

Casual Leavc : 12
"""

corrected = agent.correct(sample, 0.35)

print(corrected)