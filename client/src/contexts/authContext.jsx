import { createContext, useContext } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useLocalStorage('user', null);

  const login = (data) => setUser(data);
  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => {
  const authState = useContext(AuthContext);
  return authState;
}