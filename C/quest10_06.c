#define F_CPU 16000000L
#include <avr/io.h>
#include <avr/interrupt.h>
volatile char pattern_state0 = 0x03, pattern_state1 = 0x0C,
pattern_state2 = 0x30, pattern_state3 = 0xC0;
volatile int state0 = 0, state1 = 0, state2 = 0, state3 = 0;
ISR(INT1_vect)
{
    pattern_state0 = 0x0F;
    pattern_state1 = 0xF0;
    pattern_state2 = 0x33;
    pattern_state3 = 0xCC;
}
ISR(TIMER1_COMPA_vect)
{
    state0 = !state0;
    if(state0) PORTB |= pattern_state0;
    else PORTB &= ~ pattern_state0;
}
ISR(TIMER1_COMPB_vect)
{
    state1 = !state1;
    if(state1) PORTB |= pattern_state1;
    else PORTB &= ~ pattern_state1;
}
ISR(TIMER1_COMPC_vect)
{
    state0 = !state0;
    if(state0) PORTB |= pattern_state0;
    else PORTB &= ~ pattern_state0;
    state2 = !state2;
    if(state2) PORTB |= pattern_state2;
    else PORTB &= ~ pattern_state2;
}
ISR(TIMER1_OVF_vect)
{
    state1 = !state1;
    if(state1) PORTB |= pattern_state1;
    else PORTB &= ~ pattern_state1;
    state3 = !state3;
    if(state3) PORTB |= pattern_state3;
    else PORTB &= ~ pattern_state3;
}
int main(void)
{
    DDRB = 0xFF;
    PORTB = 0x00;
    DDRD = 0x00;
    PORTD = 0x02;
    EIMSK |= (1<<INT1);
    EICRA |= (1<<ISC11);
    OCR1A = 0x3FFF;
    OCR1B = 0x7FFF;
    OCR1C = 0xBFFF;
    TCCR1B |= (1 << CS12);
    TIMSK |= (1 << OCIE1A) | (1 << OCIE1B) | (1 << TOIE1);
    ETIMSK |= (1 << OCIE1C);
    sei();
    while(1){ }
    return 0;
}
그럼 0.25초 간격으로 0x03,0x0f,0x3c,0xf0,0xf3,0xff,0xcc,0x00 반복하는 패턴이 맞아?