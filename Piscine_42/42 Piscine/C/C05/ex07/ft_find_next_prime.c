/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/18 11:46:05 by wberger           #+#    #+#             */
/*   Updated: 2022/07/18 12:06:30 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
int	ft_is_prime(int nb)
{
	int	div;
	int	mod;

	div = 2;
	mod = 1;
	if (nb == 0 || nb == 1)
		return (0);
	if (nb < 0)
		return (0);
	while (div <= nb / div)
	{
		mod = nb % div;
		if (mod == 0)
			return (0);
		div++;
	}
	return (1);
}

int	ft_find_next_prime(int nb)
{
	while (ft_is_prime(nb) != 1)
		nb++;
	return (nb);
}
