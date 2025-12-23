import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [aadhaar, setAadhaar] = useState("");
  const navigate = useNavigate();

  const register = async () => {
    await fetch("http://127.0.0.1:5000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password, aadhaar }),
    });

    alert("Registration successful");
    navigate("/login");
  };

 return (
  <div className="center">
    <div className="card">
      <h2>Register</h2>

      <input
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <input
        placeholder="Aadhaar"
        onChange={(e) => setAadhaar(e.target.value)}
      />

      <button onClick={register}>Register</button>
    </div>
  </div>
);

}
