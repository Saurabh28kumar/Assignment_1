import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const login = async () => {
    setError("");
    try {
      const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.error || "Login failed");
        return;
      }

      localStorage.setItem("token", data.access_token);
      navigate("/dashboard");
    } catch {
      setError("Backend not reachable");
    }
  };

  return (
    <div className="center">
      {/* Wrapper keeps title & card aligned */}
      <div style={{ textAlign: "center" }}>
        <h1
          style={{
            color: "#ffffff",
            marginBottom: "25px",
            fontWeight: "600",
          }}
        >
          Secure User Profile System
        </h1>

        <div className="card">
          <h2>Login</h2>

          <input
            placeholder="Username"
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
          />

          <button onClick={login}>Login</button>

          {error && <p className="error">{error}</p>}

          <p style={{ marginTop: "15px" }}>
            New user? <Link to="/register">Register here</Link>
          </p>
        </div>
      </div>
    </div>
  );
}
