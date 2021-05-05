import React from 'react'
import SideMenu from "../SideMenu/SideMenu"
import { StyledNavbar } from "./Navbar.style"
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import LocalMallIcon from '@material-ui/icons/LocalMall';
import { SettingsInputAntennaTwoTone } from '@material-ui/icons';

export const Navbar: React.FC = () => {
    const [open, setOpen] = React.useState(false);
    
    return (
        <>
            <StyledNavbar position="static">
                <Toolbar>
                    <div className="navigation">
                        <Typography variant="h6">
                            E-FootWear
                        </Typography>
                        <Button color="inherit">Man</Button>
                        <Button color="inherit">Woman</Button>
                        <Button color="inherit">Kids</Button>
                        <Button color="inherit">Sport</Button>
                        <Button color="inherit">Sales</Button>
                    </div>
                    <div className="auth">
                        <Button variant="outlined" color="inherit">Sign In</Button>
                        <Button variant="contained" color="inherit">Sign Up</Button>
                        <LocalMallIcon />
                    </div>
                    <Typography className="logo-mobile" variant="h6">
                            E-FootWear
                        </Typography>
                    <IconButton className="menu-icon" edge="start" color="inherit" aria-label="menu" onClick={()=>setOpen(true)}>
                            <MenuIcon />
                    </IconButton>
                </Toolbar>
            </StyledNavbar>
            <SideMenu open={open} setOpen={setOpen}/>
      </>
    )
}

