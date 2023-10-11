import "../SpeechToText.css";
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import { useState } from "react";

const STT = () => {
    const [savedTranscription, setSavedTranscription] = useState(''); // To store the transcription for saving.
    const [isListening, setIsListening] = useState(false); // To track whether listening is active.

    const handleStartListening = () => {
        setIsListening(true);
        SpeechRecognition.startListening({ continuous: true, language: 'en-IN' });
    };

    const handleStopListening = () => {
        setIsListening(false);
        SpeechRecognition.stopListening();
    };

    const { transcript, browserSupportsSpeechRecognition } = useSpeechRecognition();

    const handleSaveTranscription = () => {
        // Save the transcription to a text file.
        const blob = new Blob([savedTranscription || transcript], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'transcription.txt'; // Set the file name.
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        setSavedTranscription(''); // Clear the saved transcription after saving.
    };

    if (!browserSupportsSpeechRecognition) {
        return null;
    }

    return (
        <div className="container mt-5">
            <h2 className="text-center">Speech to Text Converter</h2>
            <br />
            <p className="text-center">A React hook that converts speech from the microphone to text and makes it available to your React components.</p>

            <div className="btn-group d-flex justify-content-center mt-4">
                <button
                    className={`custom-btn ${isListening ? 'listening' : ''}`}
                    onClick={isListening ? handleStopListening : handleStartListening}
                >
                    {isListening ? 'Pause' : 'Start Listening'}
                </button>
                <button className="custom-btn" onClick={handleSaveTranscription}>Save</button>
            </div>
            <p></p>
            <div className="main-content mt-4">
                {transcript}
            </div>
        </div>
    );
};

export default STT;
